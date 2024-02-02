#!/usr/bin/env python

# reggaeton_cli.py

import argparse
import os
from reggaeton import compare_images
import cv2

def main():
    parser = argparse.ArgumentParser(description='Compare two images and highlight differences.')
    parser.add_argument('image_path1', type=str, help='Path to the first image (before).')
    parser.add_argument('image_path2', type=str, help='Path to the second image (after).')
    parser.add_argument('output_path', type=str, help='Path where the output image will be saved if differences are detected.')
    
    args = parser.parse_args()

     # Check if either of the image paths is missing
    if not os.path.isfile(args.image_path1) or not os.path.isfile(args.image_path2):
        print("Error: One or both of the image paths are missing.")
        parser.print_help()
        return
    
    result_image = compare_images(args.image_path1, args.image_path2)
    
    if result_image is not None:
        cv2.imwrite(args.output_path, result_image)
        print(f"Differences detected. Output image saved to {args.output_path}")
    else:
        print("No significant differences detected. No output image saved.")

if __name__ == "__main__":
    main()
