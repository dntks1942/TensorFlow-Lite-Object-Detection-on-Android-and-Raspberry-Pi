# Script to create CSV data file from Pascal VOC annotation files
# Based off code from GitHub user datitran: https://github.com/datitran/raccoon_dataset/blob/master/xml_to_csv.py

# import os
# import glob
# import pandas as pd
# import xml.etree.ElementTree as ET

# def xml_to_csv(path):
#     xml_list = []
#     for xml_file in glob.glob(path + '/*.xml'):
#         tree = ET.parse(xml_file)
#         root = tree.getroot()
#         for member in root.findall('object'):
#             value = (root.find('filename').text,
#                      int(root.find('size')[0].text),
#                      int(root.find('size')[1].text),
#                      member[0].text,
#                      int(member[4][0].text),
#                      int(member[4][1].text),
#                      int(member[4][2].text),
#                      int(member[4][3].text)
#                      )
#             xml_list.append(value)
#     column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
#     xml_df = pd.DataFrame(xml_list, columns=column_name)
#     return xml_df

# def main():
#     for folder in ['train','validation']:
#         image_path = os.path.join(os.getcwd(), ('images/' + folder))
#         xml_df = xml_to_csv(image_path)
#         xml_df.to_csv(('images/' + folder + '_labels.csv'), index=None)
#         print('Successfully converted xml to csv.')

# main()



import os
import glob
import pandas as pd
import json

def json_to_csv(path):
    json_list = []
    for json_file in glob.glob(path + '/*.json'):
        with open(json_file) as f:
            data = json.load(f)
            for obj in data['annotations']['object']:
                value = (
                    data['description']['image'],
                    data['description']['width'],
                    data['description']['height'],
                    obj['class'],
                    obj['points'][0]['xtl'],
                    obj['points'][0]['ytl'],
                    obj['points'][0]['xbr'],
                    obj['points'][0]['ybr']
                )
                json_list.append(value)
    
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']

    json_df = pd.DataFrame(json_list, columns=column_name)
    return json_df

def main():
    json_path = os.path.join(os.getcwd(), 'label.json')
    csv_df = json_to_csv(json_path)
    csv_df.to_csv('labels.csv', index=None)
    print('Successfully converted JSON to CSV.')

if __name__ == '__main__':
    main()





