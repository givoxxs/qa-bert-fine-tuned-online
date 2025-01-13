# QA-BERT Fine-Tuned Project

## Mô tả
Đây là repository cho dự án QA-BERT đã được fine-tuned với bộ dữ liệu SQuAD_v2 nhằm hỗ trợ trả lời câu hỏi dựa trên thông tin cung cấp. 
Để chạy dự án, bạn cần tải file model từ Google Drive và đặt vào thư mục `fine_tuned_bert_merged`.

## Hướng dẫn cài đặt

### Bước 1: Clone repository
```bash
git clone https://github.com/givoxxs/qa-bert-fine-tuned-online.git
cd qa-bert-fine-tuned-online
```

### Bước 2: Tải file model từ Google Drive
Tải file model.safetensors từ liên kết sau: [Download Model](https://drive.google.com/file/d/1ydGoaklyoElx3ki74KShL3FGOuA-xAf_/view?usp=sharing)

### Bước 3: Đặt file vào đúng thư mục
```bash
fine_tuned_bert_merged/model.safetensors
```

### Bước 4: Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### Bước 5: Chạy dự án
```bash
uvicorn app.main:app --reload

```