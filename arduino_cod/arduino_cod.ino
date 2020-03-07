#define R 2
#define G 3
#define B 4
#define T 5

String cod;

void setup() {
  Serial.begin(9600);
  pinMode(R, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(B, OUTPUT);
  pinMode(T, INPUT);
}

void loop() {

   int sw = digitalRead(T);
   if(Serial.availableForWrite()){
    Serial.println(sw);
   }
   
   if(Serial.available()){
    char aux = Serial.read();
    cod += aux;
   }
  
  // LEITURA DE CODIGOS VINDOS DO PYTHON
  
  if(cod == "069" || sw == HIGH){
    digitalWrite(R, HIGH);
    digitalWrite(G, HIGH);
    digitalWrite(B, HIGH);
    cod = "";
  }

  if(cod == "070" || sw == LOW){
    digitalWrite(R, LOW);
    digitalWrite(G, LOW);
    digitalWrite(B, LOW);
    cod = "";  
  }

  if(cod == "013"){
    digitalWrite(G, HIGH);
    cod = "";
  }
  if(cod == "016"){
    digitalWrite(G, LOW);
    cod = "";
  }
  if(cod == "014"){
    digitalWrite(R, HIGH);
    cod = "";
  }
   if(cod == "017"){
    digitalWrite(R, LOW);
    cod = "";
  }
   if(cod == "015"){
    digitalWrite(B, HIGH);
    cod = "";
  }
  if(cod == "018"){
    digitalWrite(B, LOW);
    cod = "";
  }
}
