import argparse
import speech_recognition as sr
import time


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', '-i', type=str, default='', required=True)
    parser.add_argument('--output_file', type=str, required=True)
    parser.add_argument('--method', type=str, required=True)
    args = parser.parse_args()
    return args


def speech2txt(input_file, output_file, method):
    recognizer = sr.Recognizer()
    with sr.AudioFile(input_file) as source:
        audio = recognizer.record(source)
    t_start = time.time()
    if method == "sphinx":
        results = recognizer.recognize_sphinx(audio)
    elif method == "google_api":
        pass
    else:
        raise NotImplementedError(f"Method {method} not implemented")
    t_end = time.time()
    t_duration = t_end - t_start
    print(f"Time Taken: {t_duration} seconds")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(results.text)
    print(f"Results written to {output_file}")


def main():
    print("Speech Recognition Benchmark")


if __name__ == "__main__":
    main()
