import cv2
import os
import easyocr
from dotenv import load_dotenv


load_dotenv()


class ImageBlurService:
    image_store_dir = os.getenv("IMAGE_STORE_DIR")

    def __init__(self, car_id, image_path):
        self.car_id = car_id
        self.image_path = image_path

    def _success_response(self, file_name, image_store_path):
        return {
            "success": True,
            "message": f"Successfully saved to {image_store_path}",
            "path": image_store_path,
            "file_name": f"{file_name[:-4]}_blurred.png",
        }

    def apply_blur_effect(self):
        try:
            if not self.image_path:
                raise ValueError("Image path is empty.")

            # Read the image
            img = cv2.imread(self.image_path)
            if img is None:
                raise ValueError("Could not read the image.")

            # Perform text detection
            reader = easyocr.Reader(["en"])
            results = reader.readtext(img)

            # Blur text regions
            for bbox, text, prob in results:
                if prob > 0.5:  # Consider only high-confidence detections
                    (top_left, top_right, bottom_right, bottom_left) = bbox
                    top_left = tuple([int(val) for val in top_left])
                    bottom_right = tuple([int(val) for val in bottom_right])

                    roi = img[
                        top_left[1] : bottom_right[1], top_left[0] : bottom_right[0]
                    ]
                    if roi.size != 0:
                        blurred_roi = cv2.GaussianBlur(roi, (51, 51), 30)
                        img[
                            top_left[1] : bottom_right[1], top_left[0] : bottom_right[0]
                        ] = blurred_roi

            # Save the result
            if not os.path.exists(ImageBlurService.image_store_dir):
                os.makedirs(ImageBlurService.image_store_dir)

            file_name = os.path.basename(self.image_path)
            image_store_path = os.path.join(
                ImageBlurService.image_store_dir, f"{file_name[:-4]}_blurred.png"
            )
            cv2.imwrite(image_store_path, img)
            print(f"Successfully saved to {image_store_path}")
            return self._success_response(file_name, image_store_path)

        except Exception as e:
            return {"success": False, "error": f"Error applying blur to the image: {e}"}
