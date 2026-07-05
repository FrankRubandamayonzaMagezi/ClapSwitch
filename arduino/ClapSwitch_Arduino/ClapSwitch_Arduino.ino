const int LED = 13;
bool state = false;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {

  if (Serial.available()) {

    char c = Serial.read();

    if (c == 'T') {
      state = !state;
      digitalWrite(LED, state);
    }

  }

}
