import subprocess

download_commands = [
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/hubert_base.pt -d /content/JSON-RVC-Inference/assets/hubert -o hubert_base.pt",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/rmvpe.pt -d /content/JSON-RVC-Inference/assets/rvmpe -o rmvpe.pt",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://github.com/TheNeodev/sonicrvc/raw/refs/heads/main/Sonic_model.json -d /content/JSON-RVC-Inference/models"
]

for command in download_commands:
    subprocess.run(command, shell=True)
