# 🖐 Real-Time Hand Tracking using OpenCV and MediaPipe

This Python script performs **real-time hand tracking** using your webcam with the help of [MediaPipe](https://google.github.io/mediapipe/) and [OpenCV](https://opencv.org/). It also calculates and displays the **FPS (Frames Per Second)** for performance tracking.

---

## 🚀 Features

* Detects and tracks **one hand** in real time (customizable).
* Shows **landmark points** and **connections** of the hand.
* Displays **FPS** on screen to monitor performance.

---

## 🧰 Requirements

Install the following Python packages:

```bash
pip install opencv-python mediapipe
```

If you face installation issues, try upgrading `pip`:

```bash
python -m pip install --upgrade pip
```

---

## 📝 Code Overview

* Uses **MediaPipe's Hand** model with custom configurations.
* Tracks **landmarks** of the detected hand and prints them.
* Uses **OpenCV** for displaying the live video feed with overlayed landmarks and FPS.

---

## 📸 Usage

Run the script:

```bash
python hand_tracking.py
```

* The webcam will start.
* Press **`q`** to exit the program.

---

## ⚙️ Configuration

You can configure the script to detect more than one hand by modifying the following line:

```python
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
```

Change `max_num_hands` to any value up to `2` (or more if supported).

---

## 🖼 Output

* Live webcam feed with hand landmarks and connections.
* FPS counter on the top-left corner of the screen.

---

## 📂 File Structure

```
.
├── PalmRecognition.py
└── README.md
```

---

## 📌 Notes

* Ensure your **camera permissions** are enabled.
* Performance may vary depending on your CPU/GPU and lighting conditions.

---

## 📄 License

This project is intended for learning and personal use. Credits to [MediaPipe](https://google.github.io/mediapipe/) and [OpenCV](https://opencv.org/) teams.

---

Feel free to fork or contribute! 😊
