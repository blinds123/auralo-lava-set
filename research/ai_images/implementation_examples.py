# AI Image Generation Implementation Examples
# Comprehensive code examples for e-commerce image generation

import os
import time
import base64
import requests
from PIL import Image
from io import BytesIO
from typing import List, Dict, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# =============================================================================
# OPENAI DALL-E 3 & GPT IMAGE IMPLEMENTATION
# =============================================================================

from openai import OpenAI

class OpenAIImageGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    def generate_product_image(self, product: str, style: str = "product_photo") -> str:
        """Generate a single product image using GPT Image"""
        prompts = {
            "product_photo": f"Professional e-commerce photo of {product}, clean white background, studio lighting, commercial quality, high resolution, centered composition",
            "lifestyle": f"Person wearing {product} in modern urban setting, natural lighting, lifestyle photography, authentic moment",
            "hero_banner": f"Premium {product} displayed elegantly, luxury presentation, dramatic lighting, marketing quality"
        }
        
        try:
            response = self.client.responses.create(
                model="gpt-5",
                input=prompts.get(style, prompts["product_photo"]),
                tools=[{
                    "type": "image_generation",
                    "quality": "high",
                    "size": "1024x1024",
                    "output_format": "png"
                }],
            )
            
            # Extract image data
            image_data = [
                output.result
                for output in response.output
                if output.type == "image_generation_call"
            ]
            
            if image_data:
                return image_data[0]  # Base64 encoded image
            
        except Exception as e:
            print(f"Error generating image: {e}")
            return None
    
    def batch_generate_product_views(self, product: str, views: List[str]) -> Dict[str, str]:
        """Generate multiple views of a product"""
        images = {}
        
        for view in views:
            prompt = f"Professional e-commerce photo of {product}, {view} view, clean white background, studio lighting, commercial quality"
            
            try:
                response = self.client.responses.create(
                    model="gpt-5",
                    input=prompt,
                    tools=[{"type": "image_generation", "quality": "high"}],
                )
                
                image_data = [
                    output.result
                    for output in response.output
                    if output.type == "image_generation_call"
                ]
                
                if image_data:
                    images[view] = image_data[0]
                    
            except Exception as e:
                print(f"Error generating {view} view: {e}")
                
            # Rate limiting
            time.sleep(1)
        
        return images
    
    def generate_testimonial_image(self, product: str, demographic: str = "diverse") -> str:
        """Generate ethical testimonial images with clear AI disclosure"""
        prompts = {
            "diverse": f"Authentic customer photo of person holding {product}, genuine smile, natural lighting, diverse representation, casual setting",
            "professional": f"Professional headshot style photo of person with {product}, confident expression, business casual attire",
            "young": f"Young person showcasing {product}, trendy aesthetic, social media style, good lighting"
        }
        
        prompt = prompts.get(demographic, prompts["diverse"])
        prompt += " [AI Generated Image - Not Real Person]"  # Ethical disclosure
        
        try:
            response = self.client.responses.create(
                model="gpt-5",
                input=prompt,
                tools=[{"type": "image_generation", "quality": "medium"}],
            )
            
            image_data = [
                output.result
                for output in response.output
                if output.type == "image_generation_call"
            ]
            
            return image_data[0] if image_data else None
            
        except Exception as e:
            print(f"Error generating testimonial: {e}")
            return None

# =============================================================================
# REPLICATE (FLUX & STABLE DIFFUSION) IMPLEMENTATION  
# =============================================================================

import replicate

class ReplicateImageGenerator:
    def __init__(self):
        self.api_token = os.getenv('REPLICATE_API_TOKEN')
        if self.api_token:
            os.environ["REPLICATE_API_TOKEN"] = self.api_token
    
    def generate_with_flux_pro(self, prompt: str, **kwargs) -> str:
        """Generate high-quality image with FLUX Pro"""
        default_params = {
            "prompt": prompt,
            "aspect_ratio": "1:1",
            "output_format": "png",
            "output_quality": 100,
            "num_outputs": 1
        }
        default_params.update(kwargs)
        
        try:
            output = replicate.run(
                "black-forest-labs/flux-1.1-pro",
                input=default_params
            )
            return output[0] if output else None
            
        except Exception as e:
            print(f"FLUX Pro generation error: {e}")
            return None
    
    def generate_with_flux_schnell(self, prompt: str, **kwargs) -> List[str]:
        """Generate images quickly and cost-effectively with FLUX Schnell"""
        default_params = {
            "prompt": prompt,
            "aspect_ratio": "1:1", 
            "num_outputs": 4,
            "output_format": "png"
        }
        default_params.update(kwargs)
        
        try:
            output = replicate.run(
                "black-forest-labs/flux-schnell",
                input=default_params
            )
            return output
            
        except Exception as e:
            print(f"FLUX Schnell generation error: {e}")
            return []
    
    def generate_with_stable_diffusion(self, prompt: str, negative_prompt: str = None, **kwargs) -> List[str]:
        """Generate with Stable Diffusion for maximum control"""
        default_params = {
            "prompt": prompt,
            "negative_prompt": negative_prompt or "blurry, low quality, distorted, watermark, text, shadows",
            "width": 1024,
            "height": 1024,
            "num_inference_steps": 50,
            "guidance_scale": 7.5,
            "scheduler": "DPMSolverMultistep",
            "num_outputs": 4
        }
        default_params.update(kwargs)
        
        try:
            output = replicate.run(
                "stability-ai/stable-diffusion",
                input=default_params
            )
            return output
            
        except Exception as e:
            print(f"Stable Diffusion generation error: {e}")
            return []
    
    def batch_product_generation(self, products: List[str], model: str = "flux-pro") -> Dict[str, str]:
        """Batch generate product images"""
        results = {}
        
        for product in products:
            prompt = f"Professional e-commerce photo of {product}, white background, studio lighting, commercial quality"
            
            if model == "flux-pro":
                image_url = self.generate_with_flux_pro(prompt)
            elif model == "flux-schnell":
                images = self.generate_with_flux_schnell(prompt, num_outputs=1)
                image_url = images[0] if images else None
            else:
                images = self.generate_with_stable_diffusion(prompt, num_outputs=1)
                image_url = images[0] if images else None
            
            if image_url:
                results[product] = image_url
            
            # Rate limiting
            time.sleep(0.5)
        
        return results

# =============================================================================
# IMAGE PROCESSING AND OPTIMIZATION
# =============================================================================

class ImageProcessor:
    @staticmethod
    def download_and_process(image_url: str, output_path: str) -> Dict[str, str]:
        """Download image and create optimized versions"""
        try:
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            
            # Create different sizes for various use cases
            sizes = {
                'original': image.size,
                'hero': (1200, 800),
                'product': (800, 800),
                'thumbnail': (300, 300),
                'mobile': (600, 600)
            }
            
            optimized_paths = {}
            
            for size_name, dimensions in sizes.items():
                if size_name == 'original':
                    processed = image.copy()
                else:
                    processed = image.copy()
                    processed.thumbnail(dimensions, Image.Resampling.LANCZOS)
                
                # Save in different formats
                base_name = output_path.rsplit('.', 1)[0]
                
                # PNG for transparency support
                png_path = f"{base_name}_{size_name}.png"
                processed.save(png_path, "PNG", optimize=True)
                optimized_paths[f"{size_name}_png"] = png_path
                
                # JPEG for smaller file sizes
                if processed.mode in ("RGBA", "LA", "P"):
                    processed = processed.convert("RGB")
                
                jpg_path = f"{base_name}_{size_name}.jpg"
                processed.save(jpg_path, "JPEG", quality=85, optimize=True)
                optimized_paths[f"{size_name}_jpg"] = jpg_path
            
            return optimized_paths
            
        except Exception as e:
            print(f"Error processing image: {e}")
            return {}
    
    @staticmethod
    def create_product_collage(image_paths: List[str], output_path: str) -> str:
        """Create a product collage from multiple images"""
        try:
            images = [Image.open(path) for path in image_paths]
            
            # Resize all images to same size
            target_size = (400, 400)
            resized_images = []
            for img in images:
                resized = img.copy()
                resized.thumbnail(target_size, Image.Resampling.LANCZOS)
                # Create square image with padding if needed
                square_img = Image.new('RGB', target_size, (255, 255, 255))
                offset = ((target_size[0] - resized.width) // 2, 
                         (target_size[1] - resized.height) // 2)
                square_img.paste(resized, offset)
                resized_images.append(square_img)
            
            # Create grid layout
            cols = 2
            rows = (len(resized_images) + cols - 1) // cols
            
            collage_width = cols * target_size[0]
            collage_height = rows * target_size[1]
            
            collage = Image.new('RGB', (collage_width, collage_height), (255, 255, 255))
            
            for i, img in enumerate(resized_images):
                row = i // cols
                col = i % cols
                x = col * target_size[0]
                y = row * target_size[1]
                collage.paste(img, (x, y))
            
            collage.save(output_path, "PNG", optimize=True)
            return output_path
            
        except Exception as e:
            print(f"Error creating collage: {e}")
            return ""

# =============================================================================
# COMPREHENSIVE E-COMMERCE IMAGE GENERATOR
# =============================================================================

class EcommerceImageGenerator:
    def __init__(self):
        self.openai_gen = OpenAIImageGenerator()
        self.replicate_gen = ReplicateImageGenerator()
        self.processor = ImageProcessor()
    
    def generate_product_suite(self, product_name: str, output_dir: str) -> Dict[str, any]:
        """Generate a complete suite of product images"""
        os.makedirs(output_dir, exist_ok=True)
        
        results = {
            'product_photos': {},
            'lifestyle_images': {},
            'testimonials': {},
            'social_media': {}
        }
        
        # 1. Generate main product photos (multiple angles)
        print("Generating product photos...")
        views = ['front', 'side', 'back', 'three-quarter']
        product_images = self.openai_gen.batch_generate_product_views(product_name, views)
        
        for view, image_data in product_images.items():
            if image_data:
                # Save base64 image
                image_bytes = base64.b64decode(image_data)
                file_path = os.path.join(output_dir, f"{product_name}_{view}.png")
                with open(file_path, 'wb') as f:
                    f.write(image_bytes)
                
                results['product_photos'][view] = file_path
        
        # 2. Generate lifestyle images with FLUX
        print("Generating lifestyle images...")
        lifestyle_prompt = f"Person wearing {product_name} in modern urban setting, natural lighting, lifestyle photography"
        lifestyle_url = self.replicate_gen.generate_with_flux_pro(lifestyle_prompt)
        
        if lifestyle_url:
            lifestyle_path = os.path.join(output_dir, f"{product_name}_lifestyle.png")
            optimized = self.processor.download_and_process(lifestyle_url, lifestyle_path)
            results['lifestyle_images'] = optimized
        
        # 3. Generate testimonial images (with ethical disclosure)
        print("Generating testimonial images...")
        demographics = ['diverse', 'professional', 'young']
        for demo in demographics:
            testimonial_data = self.openai_gen.generate_testimonial_image(product_name, demo)
            if testimonial_data:
                image_bytes = base64.b64decode(testimonial_data)
                file_path = os.path.join(output_dir, f"testimonial_{demo}.png")
                with open(file_path, 'wb') as f:
                    f.write(image_bytes)
                
                results['testimonials'][demo] = file_path
        
        # 4. Generate social media variations
        print("Generating social media content...")
        social_prompts = [
            f"TikTok style video thumbnail of {product_name}, trendy aesthetic, good lighting",
            f"Instagram story featuring {product_name}, modern minimalist style",
            f"Facebook ad creative showcasing {product_name}, professional photography"
        ]
        
        for i, prompt in enumerate(social_prompts):
            social_url = self.replicate_gen.generate_with_flux_schnell(prompt, num_outputs=1)
            if social_url:
                social_path = os.path.join(output_dir, f"social_media_{i+1}.png")
                optimized = self.processor.download_and_process(social_url[0], social_path)
                results['social_media'][f'variant_{i+1}'] = optimized
        
        print(f"Image generation complete! Results saved to {output_dir}")
        return results

# =============================================================================
# USAGE EXAMPLES
# =============================================================================

def main():
    # Initialize generator
    generator = EcommerceImageGenerator()
    
    # Example 1: Generate complete product suite
    product_name = "premium black hoodie"
    output_directory = "./generated_images/hoodie_suite"
    
    results = generator.generate_product_suite(product_name, output_directory)
    print("Generated images:", results)
    
    # Example 2: Individual platform usage
    openai_gen = OpenAIImageGenerator()
    
    # Generate single product image
    product_image = openai_gen.generate_product_image("black hoodie", "product_photo")
    if product_image:
        with open("single_product.png", 'wb') as f:
            f.write(base64.b64decode(product_image))
    
    # Example 3: Batch generation with Replicate
    replicate_gen = ReplicateImageGenerator()
    
    products = ["black hoodie", "white t-shirt", "blue jeans"]
    batch_results = replicate_gen.batch_product_generation(products, "flux-schnell")
    
    for product, url in batch_results.items():
        print(f"{product}: {url}")

if __name__ == "__main__":
    main()