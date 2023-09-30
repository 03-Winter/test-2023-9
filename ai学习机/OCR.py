from paddleocr import PaddleOCR

#Paddle OCR提取图片上的所有文本
def get_text(img_path, ocr):
    result = ocr.ocr(img_path, cls=True)
    # boxes = [line[0] for line in result[0]]
    texts = [line[1][0] for line in result[0]]
    texts = ''.join(texts)
    return texts


def main():
    ocr = PaddleOCR(use_angle_cls=True, lang='ch')
    text = get_text('D:/query_imgs/1XNJBjfjXTa.jpg', ocr)
    print(text)


if __name__ == '__main__':
    main()