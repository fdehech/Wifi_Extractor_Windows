import os

SSID = []
KEYS = []

C = os.popen("netsh wlan show profile").read()
C = C[C.find("User profiles") + 28::]

while C != '':
    SSID.append(C[27:C.find('\n')])
    C = C[C.find('\n') + 1:]

for i in SSID:
    P = os.popen(f"netsh wlan show profile name=\"{i}\" key=clear").read()

    key_content_index = P.find('Key Content')
    if key_content_index != -1:
        P = P[key_content_index + 25:].split('\n', 1)[0].strip()
        KEYS.append(P)
    else:
        KEYS.append("Password not found")

with open("Extracted.txt", "w") as file:
    for ssid, key in zip(SSID, KEYS):
        file.write(f"SSID: {ssid}\tPassword: {key}\n")

print("Extraction complete. Results saved in Extracted.txt.")
