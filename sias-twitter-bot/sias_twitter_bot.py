import tweepy, time
from firebase import firebase

fb = firebase.FirebaseApplication('firebaseURL', None)



print('this is my twitter bot')

COMSUMER_KEY = 'CONSUMER_KEY'
CONSUMER_SECRET = 'CONSUMER_SECRET'
ACCESS_KEY = 'ACCESS_KEY'
ACCESS_SECRET = 'ACCESS_SECRET'

auth = tweepy.OAuthHandler(COMSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def get_last_seen_id():
        last_seen_id = fb.get('/lastTweetSeen/last_seen_id', None)
        print('last_seen_id: ', last_seen_id)
        return last_seen_id

def post_last_seen_id(last_seen_id):
        fb.patch('/lastTweetSeen', {'last_seen_id':last_seen_id})
        return

def get_status():
        status_ground = fb.get('/Estado/Umidade', None)['Status']
        print('Status ground: ', status_ground)
        status_temperature = fb.get('/Estado/Temperatura', None)['Status']
        print('Status temperature: ', status_temperature)
        status_light = fb.get('/Estado/Luminosidade', None)['Status']
        print('Status light: ', status_light)
        status = 'Solo: ' + status_ground + '; Temperatura: ' + status_temperature + '; Luminosidade: ' + status_light
        return status

def reply_to_tweets():
        print('retriving and replying to tweets...')
        last_seen_id = get_last_seen_id()
        mentions = api.mentions_timeline(
                                        last_seen_id,
                                        tweet_mode='extended')
        for mention in reversed(mentions):
                print(str(mention.id) + ' - ' + mention.full_text)
                last_seen_id = mention.id
                post_last_seen_id(last_seen_id)
                if '#sias' in mention.full_text.lower():
                        status = get_status()
                        print('found #sias')
                        print('respond back...')
                        try:
                                api.update_status('@' + mention.user.screen_name + ' o status é ' + status, in_reply_to_status=mention.id)
                        except tweepy.TweepError as error:
                                if error.api_code == 187:
                                        api.update_status('@' + mention.user.screen_name + ' status é ' + status, in_reply_to_status=mention.id)
                                else:
                                        raise error

def run_my_twitter_bot():
        while True:
                reply_to_tweets()
                time.sleep(5)

run_my_twitter_bot()
