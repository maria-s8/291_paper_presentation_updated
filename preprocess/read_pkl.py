import pickle
import re, os, time, json, pickle

if __name__ == '__main__':

    design_json = f"../design_rtl_timer_pwr.json"

    global phase, cmd, label_cmd
    # cmd = 'sog'
    cmd = 'xag'
    # cmd = 'aig'
    # cmd = 'aimg'

    label_cmd = "init"
    #label_cmd = "route"
    
    #label_cmd = "init_word"
    #label_cmd = "route_word"

    phase = 'SYN'
    assert phase in ['SYN', 'PREOPT', 'PLACE', 'CTS', 'ROUTE']

    with open(design_json, 'r') as f:
        design_data = json.load(f)

    
    design_name = "TinyRocket"
    bench_list = ['iscas', 'itc', 'opencores','VexRiscv', 'chipyard', 'riscvcores', 'NVDLA']
    # bench_list = ['chipyard', 'riscvcores', 'NVDLA']

    with open(f"./test_feat_label_timing/{design_name}_{cmd}_{label_cmd}.pkl", 'rb') as f:
        data = pickle.load(f)

    print(type(data))  # See what kind of object it is
   
    for i, item in enumerate(data):
        print(f"\n--- Entry {i} ---")
        for k, v in item.items():
            print(f"{k}: {v}")

    #print(data, "\n")        # View the contents (if small)