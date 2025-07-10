import subprocess

def collect_telemetry():
    """
    Collects system telemetry using various tools.
    """
    result_perf = subprocess.run(["perf", "stat", "-e", "cycles,instructions,cache-misses,L1-dcache-load-misses,LLC-load-misses", "--", "sleep", "5"], capture_output=True, text=True)
    print(result_perf.stdout)

if __name__ == "__main__":
    collect_telemetry()
