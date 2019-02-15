from matting import matting, load_image, save_image, blend

# Input paths
image_path  = "plant_image.jpg"
trimap_path = "plant_trimap.png"
# Output path
alpha_path  = "plant_alpha.png"

# Limit image size to make demo run faster
height = 128

# Load input images
image  = load_image( image_path, "RGB" , "BILINEAR", height=height)
trimap = load_image(trimap_path, "GRAY", "NEAREST" , height=height)

# Calculate alpha
method = "closed_form"
# other methods:
#method = "knn"
#method = "lkm"
alpha = matting(image, trimap, method)

# Save alpha
save_image(alpha_path, alpha)

# Load new background image
new_background = load_image(
    path="background.png",
    mode="RGB",
    interpolation="BILINEAR",
    width=image.shape[1],
    height=image.shape[0])

# Compose image onto new background
image_on_new_background = blend(image, new_background, alpha)

# Save image on new background
save_image("image_on_new_background.png", image_on_new_background)
