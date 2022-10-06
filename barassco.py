import csv
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


id = 446182
for i in tqdm(range(71850)):
  try:
      request = requests.get('https://lawyers.gov.iq/wp-admin/admin-ajax.php?action=ajax_card&id='+str(id))
      soup_data = BeautifulSoup(request.text, 'html.parser')
      list = soup_data.find_all('h4')
      data = [list[0].text,list[1].text,list[2].text]
  

      with open('iraqi_bar_association.csv', 'a', encoding='UTF8', newline='') as f:
          writer = csv.writer(f)
          writer.writerow(data)
      id +=1
  except:
      with open('failed.csv', 'a', encoding='UTF8', newline='') as f:
          writer = csv.writer(f)
          writer.writerow(str(id))
      id +=1
