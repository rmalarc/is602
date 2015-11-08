
import scipy.ndimage as ndimage
import numpy as np
import matplotlib.pyplot as plt
import sys

# Author: Mauricio Alarcon <rmalarc@msn.com>


class ImageHelper:
    def __init__(self):
        self.image = []
        self.image = np.ndarray(self.image)
        pass

    def load_image(self,filename):
        try:
            self.image = ndimage.imread(filename,flatten=True, mode='LA')
        except:
            print "Unable to open image: ", sys.exc_info()[0]
            raise

    def gaussian_filter(self,sigma=2):
        return ndimage.gaussian_filter(self.image, sigma)

    def threshold_image(self,threshold):
        return self.image >= threshold

    def detect_objects(self):
        return ndimage.label(self.image)

class DetectImageObjects:
    def __init__(self,filename):
        self.image_raw = ImageHelper()
        self.image_bw = ImageHelper()
        self.image_w_objects = ImageHelper()
        self.detected_object_ct = None
        self.detected_centroids = None

        self.load_raw_image(filename)
        pass

    def load_raw_image(self,filename):
        self.image_raw.load_image(filename)

    def denoise_raw_image(self,sigma=3):
        self.image_raw.image = self.image_raw.gaussian_filter(sigma)

    def threshold_image(self,threshold):
        self.image_bw.image = self.image_raw.threshold_image(threshold)

    def detect_edges(self):
        sx = ndimage.sobel(self.image_raw.image, axis=0, mode='constant')
        sy = ndimage.sobel(self.image_raw.image, axis=1, mode='constant')
        image_edges = np.hypot(sx, sy)
        t = image_edges.mean()*1.4
        image_edges[image_edges<t]=1
        image_edges[image_edges>=t]=0
        self.image_bw.image = image_edges


    def detect_objects(self):
        self.image_w_objects.image, self.detected_object_ct = self.image_bw.detect_objects()
        centroids = ndimage.measurements.center_of_mass(self.image_bw.image
                                                        , self.image_w_objects.image
                                                        , list(range(1,self.detected_object_ct+1)))
        self.detected_centroids = np.array(centroids)


    def show_resulting_images(self):
        fig, (ax1,ax2,ax3) = plt.subplots(1,3, figsize=(8, 8))
        ax1.imshow(self.image_raw.image,cmap=plt.cm.gray)
        ax1.set_title('Grey-scale and De-noised Image')
        ax1.axis('off')

        ax2.imshow(self.image_bw.image,cmap=plt.cm.gray)
        ax2.set_title('B&W Image')
        ax2.axis('off')

        ax3.imshow(self.image_raw.image,cmap=plt.cm.gray)
        ax3.set_title('B&W Image - With Objects')
        ax3.axis('off')

        x = list(self.detected_centroids[:,1])
        y = list(self.detected_centroids[:,0])

        plt.scatter(x=x,y=y, c='y', s=50)

        plt.show()

    def print_results(self):
        print "\nRESULTS:\n\nI detected %i objects. Here are the coordinates:\n" % self.detected_object_ct
        print self.detected_centroids




if __name__ == "__main__":

    filename = './images.for.lesson.8/objects.png'

    image1 = DetectImageObjects(filename)
    image1.denoise_raw_image()
    image1.threshold_image(image1.image_raw.image.mean())

    image1.detect_objects()
    image1.show_resulting_images()
    image1.print_results()

    filename2 = './images.for.lesson.8/circles.png'
    image2 = DetectImageObjects(filename2)
    image2.denoise_raw_image()

    # Increase the threshold so we don't catch the antialias
    image2.threshold_image(image2.image_raw.image.mean()+2*image2.image_raw.image.std())

    image2.detect_objects()
    image2.show_resulting_images()
    image2.print_results()

    # Detect objects by first attempting to trace an outline around the peppers
    filename3 = './images.for.lesson.8/peppers.png'
    image3 = DetectImageObjects(filename3)
    image3.denoise_raw_image()

    image3.detect_edges()
    image3.detect_objects()
    image3.show_resulting_images()
    image3.print_results()

