import cv2
import math
 
# Lists to store the points
 
def drawCoordinates(action, x, y, flags, userdata):
 
  # Action to be taken when left mouse button is released
  if action==cv2.EVENT_LBUTTONUP:
    # Mark the vertex
    cv2.circle(source, (x,y), 1, (255,255,0),2, cv2.LINE_AA )
    cv2.putText(source,"({}, {})".format(str(x),str(y)),
              (x,y-10),  cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255))
 
source = cv2.imread("horse.jpg",1)
# Make a dummy image, will be useful to clear the drawing
dummy = source.copy()
cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawCoordinates)
k = 0
# loop until escape character is pressed
while k!=27 :
  
  cv2.imshow("Window", source)
#   cv2.putText(source,'''Click on the image to get the coordinates, press ESC to exit''' ,
#               (10,30), cv2.FONT_HERSHEY_SIMPLEX, 
#               0.7,(255,255,255), 2 );
  k = cv2.waitKey(20) & 0xFF
  
  # Another way of cloning
  if k==99:
    source= dummy.copy()
 
cv2.destroyAllWindows()
