{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "0d51cb43",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "input a distance or a weight amount 0.9144 m\n",
      "Number: 0.9144\n",
      "Unit: m\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "data = input(\"input a distance or a weight amount \")\n",
    "\n",
    "match = re.match(r'(\\d+(\\.\\d+)?)\\s+([a-zA-Z]+)', data)\n",
    "\n",
    "if match:\n",
    "    data_number = float(match.group(1))  # Extract the number\n",
    "    data_unit = match.group(3)    # Extract the unit (text)\n",
    "    \n",
    "    print(\"Number:\", data_number)\n",
    "    print(\"Unit:\", data_unit)\n",
    "else: print(\"error\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "ede87900",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The convention result is 1.0 yd\n"
     ]
    }
   ],
   "source": [
    "match data_unit:\n",
    "    \n",
    "    case \"cm\":\n",
    "        result_number = data_number / 2.54\n",
    "        result_unit = \"in\"\n",
    "    case \"in\":\n",
    "        result_number = data_number * 2.54\n",
    "        result_unit = \"cm\"\n",
    "        \n",
    "    case \"yd\":\n",
    "        result_number = data_number * 0.9144\n",
    "        result_unit = \"m\"\n",
    "    case \"m\":\n",
    "        result_number = data_number / 0.9144\n",
    "        result_unit = \"yd\"\n",
    "        \n",
    "    case \"oz\":\n",
    "        result_number = data_number * 28.3495\n",
    "        result_unit = \"gm\"\n",
    "    case \"gm\":\n",
    "        result_number = data_number / 28.3495\n",
    "        result_unit = \"cm\"\n",
    "        \n",
    "    case \"lb\":\n",
    "        result_number = data_number * 0.453592\n",
    "        result_unit = \"kg\"\n",
    "    case \"kg\":\n",
    "        result_number = data_number / 0.453592\n",
    "        result_unit = \"lb\"\n",
    "        \n",
    "        \n",
    "print(\"The convention result is\", result_number, result_unit)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16bb56c8",
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
