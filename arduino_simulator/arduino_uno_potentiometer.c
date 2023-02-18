// https://docs.arduino.cc/built-in-examples/basics/AnalogReadSerial

String recv_buf;

String data_rcd = "****RCD";
String data_hdd = "****HDD";
String data_rld = "****RLD";

char buffer[5];

char* formatForPrint(int foo)
{
  sprintf(buffer,"%04d", foo);
  return buffer; 
}

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
  while (!Serial.available());
  recv_buf = Serial.readString();
  recv_buf.trim();

  if (recv_buf.startsWith(data_rcd)) {
    Serial.println(get_hw_config_data(recv_buf));
    Serial.flush();
  }
  else if (recv_buf.startsWith(data_hdd)) {
    Serial.println(get_requested_data(recv_buf));
    Serial.flush();
  }
  else if (recv_buf.startsWith(data_rld)) {
    Serial.println(get_requested_data(recv_buf));
    Serial.flush();
  }
  else {
    ;
  }
}

String get_hw_config_data(String recv_buf){
  String data_hcd = "****HCDVB01CID1COMP001ACOMP001BCOMP002A####";    //HCD
  return data_hcd;
}

String get_requested_data(String recv_buf){
  String rda_header = "****RDA";
  String vm_id = "VM01";
  String vb_id = "VB01";
  String clnt_id = "CID1";
  String comp_001 = "COMP001A";
  String comp_001_data = String(formatForPrint(analogRead(A0)));
  String eof = "####";
  
  String data_rda = rda_header+vm_id+vb_id+clnt_id+comp_001+comp_001_data+eof;        //RDA
  
  return data_rda;
}
