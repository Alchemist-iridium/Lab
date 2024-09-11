{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2cab7799",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the radius of a circle10\n",
      "The circle with radius 10.0  has an area of 314.16 and a perimeter of 62.83\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "r = float(input(\"enter the radius of a circle\")) #input the radius\n",
    "\n",
    "peri = 2* math.pi *r \n",
    "area = math.pi * r**2 #calculate the perimeter and area\n",
    "\n",
    "peri = round(peri,2)\n",
    "area = round(area,2)\n",
    "\n",
    "print(\"The circle with radius\", r,\" has an area of\",area,\"and a perimeter of\",peri)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52e32ac8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
