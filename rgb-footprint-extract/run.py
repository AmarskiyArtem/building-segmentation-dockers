import argparse
import adapter

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input_path",
        type=str,
        help="Path to the images",
        default="/rgb-footprint-extract/rgb-footprint-extract/input/",
    )
    
    parser.add_argument(
        "--output_path", 
        type=str,
        help="Path to the segmentation masks",
        default="/rgb-footprint-extract/rgb-footprint-extract/output/",
    )  

    args = parser.parse_args()
    adapter.Adapter(
        input_path=args.input_path,
        output_path=args.output_path
    ).run()