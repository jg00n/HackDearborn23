import csv

sensor_Manifest = 'sensor.csv'

TEMP_MIN = 0
TEMP_MAX = 100
PRESURE_MIN = 0
PRESURE_MAX = 100

sensor_Veh = {'Temp': 0.0, 'Presh': 0, 'Status': True, 'Faulty': False}
key_position = {
  'ACC': True,
  'RUN': False,
  'CRANK': False,
  'LOCKED': False  #if a sensor is faulty we will lock the position
}
ignition = True


def Read_data():
  try:
    with open(sensor_Manifest, 'r') as sensor_log:
      # Create CSV read object
      sensor_in = csv.DictReader(sensor_log)
      # print(type(sensor_in))
      for line in sensor_in:
        print(line)
      # Hold information in dictionary

      for key, value in sensor_Veh.items():
        if key in sensor_in:
          sensor_Veh[key] = sensor_in[key]

  except FileNotFoundError:
    print(f"No sensor manifest found!\n")
    return


def Write_data():
  sensor_dict = {}
  sensor_dict.update(sensor_Veh)

  try:
    with open(sensor_Manifest, 'w', newline='') as csv_file:
      fieldnames = ['key', 'value']
      writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
      writer.writeheader()
      for key, value in sensor_dict.items():
        try:
          writer.writerow({'key': key, 'value': value})
        except Exception as e:
          print(f"Error: Unable to update {key}: {value}!")
  except Exception as e:
    print(f"Error connected to sensor manifest!: {e}")


def Detect_Fault():
  for key, value in sensor_Veh.items():  #can take it out
    #call the leaking bucket algorethem instead
    #if leaking bucket changes faulty to false
    if key == 'Faulty':
      if (value == True):
        for key, valu in key_position.items():
          key_position.update({key: False})


#if the leaking bucket retrunes true after false , then the keyposition will be unstuck

      if (value == False):
        for key, value in key_position.items():
          key_position.update({key: True})

    if (key == 'Temp'):
      if value < TEMP_MIN:
        print("fault due to low temp")
      if value > TEMP_MAX:
        print("fault due to high temp")
    if (key == 'Presh'):
      if value < PRESURE_MIN:
        print("fault due to low pressure")
      if value > PRESURE_MAX:
        print("fault due to High pressure")


def main():
  Read_data()
  #call fun
  Detect_Fault()
  # for key, value in sensor_Veh.items():
  #   print(key,"-",value)
  for key, value in key_position.items():
    print(key, "-", value)
  #Write_data()


main()
