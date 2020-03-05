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
/*
  while(Serial.availableForWrite()){
    delay(10);
    int sw = digitalRead(T);
    if(sw == HIGH){
      Serial.write("L");
    }
    if(sw == LOW){
      Serial.write("D");
    }
  }*/
  
  while(Serial.available()){
    delay(10);
    char aux = Serial.read();
    cod += aux;
  }

  if(cod == "069"){
    digitalWrite(R, HIGH);
    digitalWrite(G, HIGH);
    digitalWrite(B, HIGH);
    cod = "";
  }

  if(cod == "070"){
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
