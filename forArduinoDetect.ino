void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(A5, OUTPUT);
  pinMode(A1, OUTPUT);

}
int val = 0;
unsigned long time = 0;
bool dataBuzz = 0;

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    val = char(Serial.read()) - '0';
    Serial.write("\n");
    digitalWrite(LED_BUILTIN, val);
    digitalWrite(A5, val);
//    digitalWrite(A1, val);
    if (val){
      tone(A1, 1000);
    }
    else{
      noTone(A1);
    }
      
  }
}
