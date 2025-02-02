import edge_tts

TEXT = "メロスは激怒した。必ず、かの邪智暴虐の王を除かなければならぬと決意した。メロスには政治がわからぬ。メロスは、村の牧人である。笛を吹き、羊と遊んで暮して来た。けれども邪悪に対しては、人一倍に敏感であった。きょう未明メロスは村を出発し、野を越え山越え、十里はなれた此のシラクスの市にやって来た。"
VOICE = "ja-JP-KeitaNeural"
OUTPUT_FILE = "dazai_ja-JP-KeitaNeural.mp3"


def main() -> None:
    communicate = edge_tts.Communicate(TEXT, VOICE)
    communicate.save_sync(OUTPUT_FILE)


if __name__ == "__main__":
    main()
