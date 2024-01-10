import queue
import time

request_queue = queue.Queue()

def generate_request():
    request_data = {"id": request_queue.qsize() + 1, "timestamp": time.time()}
    request_queue.put(request_data)
    print(f"Заявка {request_data['id']} створена.")

def process_request():
    if not request_queue.empty():
        # Видалити заявку з черги
        request_data = request_queue.get()
        print(f"Заявка {request_data['id']} оброблена.")
    else:
        print("Черга порожня. Очікуємо нові заявки.")


# Головний цикл програми
def main():
    while True:
        try:
            generate_request()
            process_request()
            time.sleep(1)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
