from utils.input_handler import get_text_input, get_voice_input
from utils.video_generator import get_video_paths_for_input, play_merged_video_live

def main():
    mode = input("Choose input mode (1: Text, 2: Voice): ")
    
    if mode == "1":
        user_input = get_text_input()
    else:
        user_input = get_voice_input()

    if user_input:
        print(f"✅ Input received: {user_input}")
        
        # Get list of video file paths
        video_paths = get_video_paths_for_input(user_input)

        if video_paths:
            play_merged_video_live(video_paths)
        else:
            print("❌ No matching videos found.")
    else:
        print("❌ Could not process input.")

if __name__ == "__main__":
    main()

