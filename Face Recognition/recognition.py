import face_recognition
import cv2

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
chris_image = face_recognition.load_image_file("chris.jpg")
chris_face_encoding = face_recognition.face_encodings(chris_image)[0]

# Load a sample picture and learn how to recognize it.
ben_image = face_recognition.load_image_file("ben.jpg")
ben_face_encoding = face_recognition.face_encodings(ben_image)[0]

# Load a sample picture and learn how to recognize it.
katie_image = face_recognition.load_image_file("katie.JPG")
katie_face_encoding = face_recognition.face_encodings(katie_image)[0]

# Load a sample picture and learn how to recognize it.
neil_image = face_recognition.load_image_file("neil.jpg")
neil_face_encoding = face_recognition.face_encodings(neil_image)[0]

# Load a sample picture and learn how to recognize it.
lyndi_image = face_recognition.load_image_file("lyndi.jpg")
lyndi_face_encoding = face_recognition.face_encodings(lyndi_image)[0]

# Load a sample picture and learn how to recognize it.
rolando_image = face_recognition.load_image_file("rolando.jpg")
rolando_face_encoding = face_recognition.face_encodings(rolando_image)[0]

# Load a sample picture and learn how to recognize it.
steve_image = face_recognition.load_image_file("steve.jpg")
steve_face_encoding = face_recognition.face_encodings(steve_image)[0]

# Load a sample picture and learn how to recognize it.
elliott_image = face_recognition.load_image_file("elliott.jpeg")
elliott_face_encoding = face_recognition.face_encodings(elliott_image)[0]

# Load a sample picture and learn how to recognize it.
andy_image = face_recognition.load_image_file("andy.jpg")
andy_face_encoding = face_recognition.face_encodings(andy_image)[0]

### Load a second sample picture and learn how to recognize it.
##biden_image = face_recognition.load_image_file("biden.jpg")
##biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    chris_face_encoding,
    steve_face_encoding,
    neil_face_encoding,
    lyndi_face_encoding,
    rolando_face_encoding,
    elliott_face_encoding,
    ben_face_encoding,
    katie_face_encoding,
    andy_face_encoding
    
]
known_face_names = [
    "Chris",
    "Steve Jobs",
    "Neil",
    "Lyndi",
    "Rolando",
    "Elliott",
    "Ben",
    "Katie",
    "Andy"
    
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
