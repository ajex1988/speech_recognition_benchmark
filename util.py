from pydub import AudioSegment
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file', '-i', default='data/test_clip.mp3')
    parser.add_argument('--output-file', '-o', default='data/test_clip.wav')
    args = parser.parse_args()
    return args


def mp3_to_wav(in_path, out_path):
    rec = AudioSegment.from_mp3(in_path)
    rec.export(out_path, format="wav")


def main():
    args = get_args()
    mp3_to_wav(args.input_file, args.output_file)


if __name__ == "__main__":
    main()
