import time
import random
from queue import Queue

requests_queue = Queue()
request_counter = 0

def generate_request():
    global request_counter
    request_counter += 1
    
    request_id = f"ЗАЯВКА-{request_counter:04d}"
    
    requests_queue.put(request_id)
    
    print(f"Створено та додано: {request_id} (Приблизний розмір черги: {requests_queue.qsize()})")

def process_request():
    
    if not requests_queue.empty():
        
        request_to_process = requests_queue.get()
        
        print(f"Обробка: {request_to_process}...")
        time.sleep(random.uniform(0.1, 0.5))
        
        requests_queue.task_done()
        
        print(f"Завершено: {request_to_process} (Приблизний розмір черги: {requests_queue.qsize()})")
    else:
        print("Черга заявок пуста. Очікування нових... ")

def main_loop():
    
    print("--- СЕРВІСНИЙ ЦЕНТР: СТАРТ ІМІТАЦІЇ (Queue) ---")
    
    max_iterations = 20
    i = 0
    
    try:
        while i < max_iterations:
            generate_request()
            
            time.sleep(random.uniform(0.1, 0.3))

            process_request()
            if random.random() < 0.3:
                process_request()

            print("-" * 30)
            i += 1
            
        print("\n--- ГОЛОВНИЙ ПОТІК ЗУПИНЕНО. ОБРОБКА ЗАЛИШКІВ ЧЕРГИ ---")
        
        while not requests_queue.empty():
             process_request()
            
    except KeyboardInterrupt:
        print("\n--- ІМІТАЦІЯ ПЕРВАНАЖЕННЯ (ПРИМУСОВА ЗУПИНКА) ---")
        print(f"Залишилося необроблених заявок: {requests_queue.qsize()}")
    
    print("--- СЕРВІСНИЙ ЦЕНТР: КІНЕЦЬ ІМІТАЦІЇ ---")


if __name__ == "__main__":
    main_loop() 