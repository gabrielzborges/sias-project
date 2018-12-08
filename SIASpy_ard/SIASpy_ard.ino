// --- Variaveis globais ---
int tempoLeitura = 1000;    //intervalo de leitura em milisegundo

// --- Variaveis que armazenaram a umidade, luminosidade e temperatura ideal para cada semente ---
int U, L;
float T;

// --- Mapeando as portas ---
#define analogi A0
#define digital 0
#define LM35 A1
#define LDR A3


void setup(){
  Serial.begin(9600);
  pinMode(analogi , INPUT);
  pinMode(digital , INPUT);
}


void loop(){
  read_umidade();
  read_temperatura();
  read_luminosidade();
  delay(tempoLeitura);
}


int receive_Umidade(){
 int umd = Serial.parseInt();
 return umd;
}

float receive_Temperatura(){
 float temp = Serial.parseFloat();
 return temp;
}


//funcao que le a umidade
//parametros so os leveis de umidade
void read_umidade(){
  int umidade = analogRead(analogi);    //le valor do analogico
  
  Serial.print("Umidade: ");
  Serial.print(umidade);
  Serial.print("; - ");
}

void read_temperatura(){
  float temperatura = (float(analogRead(LM35))*5/(1023))/0.01;
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.print("; - ");
}

void read_luminosidade(){
  int luminosidade = analogRead(LDR);
  Serial.print("Luminosidade: ");
  Serial.print(luminosidade);
  Serial.println(";");
}
