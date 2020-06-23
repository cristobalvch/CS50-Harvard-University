#include "helpers.h"
#include <math.h>
#include <cs50.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE pixel = image[i][j];
            int average = round((pixel.rgbtRed + pixel.rgbtGreen + pixel.rgbtBlue) / 3.0);
            image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j].rgbtBlue = average;
        }
    }
}

int cap(int value)
{
    return value > 255 ? 255 : value;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
     for (int i =0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE pixel = image[i][j];
            int originalRed = pixel.rgbtRed;
            int originalBlue = pixel.rgbtBlue;
            int originalGreen = pixel.rgbtGreen;
            image[i][j].rgbtRed = cap(round(0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue));
            image[i][j].rgbtGreen = cap(round(0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue));
            image[i][j].rgbtBlue = cap(round(0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue));
        }
    }
}

void swap(RGBTRIPLE * pixel1, RGBTRIPLE * pixel2)
{
    RGBTRIPLE temp = *pixel1;
    *pixel1 = *pixel2;
    *pixel2 = temp;
}
// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            swap(&image[i][j], &image[i][width - 1 - j]);
        }
    }
}

bool is_valid_pixel(int i, int j, int height, int width)
{
    return i >=0 && i < height && j >=0 && j < width;
}

RGBTRIPLE get_blurred_pixel(int i, int j, int height, int width, RGBTRIPLE image[height][width])
{
    int RedValue, BlueValue, GreenValue; RedValue = BlueValue = GreenValue = 0;
    int numOfValidPixels = 0;

    for (int di = -1; di <= 1; di++)
    {
        for (int dj = -1; dj <= 1; dj++)
        {
            int new_i = i + di;
            int new_j = j +dj;
            if (is_valid_pixel(new_i, new_j, height, width))
            {
                numOfValidPixels++;
                RedValue += image[new_i][new_j].rgbtRed;
                BlueValue += image[new_i][new_j].rgbtBlue;
                GreenValue += image[new_i][new_j].rgbtGreen;
            }
        }
    }
    RGBTRIPLE blurred_pixel;
    blurred_pixel.rgbtRed = round((float) RedValue / numOfValidPixels);
    blurred_pixel.rgbtGreen = round((float) GreenValue / numOfValidPixels);
    blurred_pixel.rgbtBlue = round((float) BlueValue / numOfValidPixels);
    return blurred_pixel;
}


// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
  RGBTRIPLE new_image[height][width];
  for (int i = 0; i < height; i++)
  {
      for (int j = 0; j < width; j++)
      {
          new_image[i][j] = get_blurred_pixel(i, j, height, width, image);
      }
  }

  for (int i = 0; i < height; i++)
    for (int j = 0; j < width; j++)
        image[i][j] = new_image[i][j];
}
