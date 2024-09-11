{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "9d6950fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the length of a side of the triangle1\n",
      "enter the length of the other side of the triangle1\n",
      "The hypotenuse is 1.41\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "a = float(input(\"enter the length of a side of the triangle\"))\n",
    "b = float(input(\"enter the length of the other side of the triangle\")) #input the two sides\n",
    "\n",
    "c = math.sqrt(a**2+b**2) #calculate hypotenuse\n",
    "\n",
    "c = round(c,2) #round the digit\n",
    "\n",
    "print(\"The hypotenuse is\",c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4e7c26e",
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
