import cv2
import json
import os
import glob

# 해충 class를 숫자 index에서 str index로
def class_name(input):
    if input in [1,4,5,6,8,10,17,20]:
        return 'moth'
    elif input in [7,14,15,16,19]:
        return 'stink'
    elif input in [13]:
        return 'aphid'
    elif input in [2]:
        return 'occidentalis'
    elif input in [3]:
        return 'tabaci'
    elif input in [9]:
        return 'bee'
    elif input in [11]:
        return 'butterfly'
    elif input in [18]:
        return 'ladybug'
    elif input in [12]: 
        return 'striolata'
    else: return 'normal'
    

def resize_image_and_annotation(input_dir, output_img_dir, output_json_dir, postfix, target_size=(800, 600)):
    # 지정된 디렉토리에서 jpg 파일들의 목록을 가져옴
    img_files = glob.glob(os.path.join(input_dir, postfix))

    for img_file in img_files:
        json_file = img_file.split('.')[0]+ '.json'
        #print(json_file)
        # 이미지와 JSON 파일이 모두 존재하는 경우에만 처리
        if os.path.exists(json_file):
            #print("exist")
            # 이미지 로드
            img = cv2.imread(img_file)
            h, w = img.shape[:2]

            # 이미지 리사이즈
            resized_img = cv2.resize(img, target_size, interpolation = cv2.INTER_AREA)

            # 리사이즈된 이미지 저장
            img_filename = os.path.basename(img_file)
            cv2.imwrite(os.path.join(output_img_dir, img_filename), resized_img)

            # 가로, 세로 비율 계산
            width_ratio = target_size[0] / w
            height_ratio = target_size[1] / h

            # JSON 파일 로드
            with open(json_file, 'r') as f:
                data = json.load(f)

            # Bounding box 좌표 수정
            for obj in data['annotations']['object']:
                obj['class'] = class_name(obj['class'])
                for point in obj['points']:
                    point['xtl'] = (int)(point['xtl'] * width_ratio)
                    point['ytl'] = (int)(point['ytl'] * height_ratio)
                    point['xbr'] = (int)(point['xbr'] * width_ratio)
                    point['ybr'] = (int)(point['ybr'] * height_ratio)

            # JSON에서 이미지의 width와 height도 업데이트
            data['description']['width'] = target_size[0]
            data['description']['height'] = target_size[1]

            # number to str class name
            
            # 수정된 JSON 파일 저장
            json_filename = os.path.basename(json_file)
            with open(os.path.join(output_json_dir, json_filename), 'w') as f:
                json.dump(data, f,ensure_ascii=False, indent=4)
        else:
            print("No file matching")


def main():
    input_dir = '/home/shin/Graduation_Project/data/images'
    output_img_dir = '/home/shin/Graduation_Project/data/result'
    output_json_dir = '/home/shin/Graduation_Project/data/result'
    resize_image_and_annotation(input_dir, output_img_dir, output_json_dir, '*.JPG')
    resize_image_and_annotation(input_dir, output_img_dir, output_json_dir, '*.jpg')


if __name__ == "__main__":
    main()
    
