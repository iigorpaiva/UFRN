#define R 2
#define G 3
#define B 4

String cod;

void setup() {
  Serial.begin(9600);
  pinMode(R, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(B, OUTPUT);
}

void loop() {
  
  while(Serial.available()){
    delay(10);
    char aux = Serial.read();
    cod += aux;
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
  delay(15);
}
