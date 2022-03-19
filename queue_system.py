from multiprocessing import Process, Semaphore
import time
import argparse

free_resources = Semaphore(4)

def handle_api_request(seconds):
    time.sleep(seconds)

def server_task(seconds):
    free_resources.acquire()
    handle_api_request(seconds)
    free_resources.release()

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--requests', type=int, required=True)
    parser.add_argument('--tracking_seconds', type=float, required=True)
    return parser
    
if __name__ == '__main__':
    args = get_parser().parse_args()

    requests = args.requests
    tracking_seconds = args.tracking_seconds

    processes = []
    for request_id in range(requests):
        p = Process(target=server_task, args=(request_id,))
        p.start()
        processes.append(p)

    while True:
        statuses = [p.is_alive() for p in processes]
        pids = [str(p.pid) for p in processes]
        exit_codes = [str(p.exitcode) if p.exitcode != None else '-' for p in processes]
        
        print()
        print('PID\t\t' + '\t'.join(pids))
        print('Status (Alive)\t' + '\t'.join([str(status) for status in statuses]))
        print('Exit Code\t' + '\t'.join(exit_codes))
        if not sum(statuses):
            success = ['yes' if p.exitcode == 0 else 'No' for p in processes]
            print('Success\t\t' + '\t'.join(success))
            break
        time.sleep(tracking_seconds)

    for p in processes:
        p.terminate()
