import subprocess

def collect_telemetry():
    """
    Collects system telemetry using various tools.
    """
    print("ForgeMind Telemetry: Collecting hardware and runtime metrics...")
    
    # Using lscpu
    print("--- lscpu ---")
    subprocess.run(["lscpu"])
    
    # Using perf stat (example)
    print("--- perf stat (example) ---")
    subprocess.run(["perf", "stat", "-e", "cycles,instructions", "--", "sleep", "1"])

if __name__ == "__main__":
    collect_telemetry()
