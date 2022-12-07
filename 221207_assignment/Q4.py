{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "df = pd.read_csv('score.csv')\n",
    "\n",
    "low_cutoff_score = df[('TotalScore')].quantile(0.25)\n",
    "high_cutoff_score = df[('TotalScore')].quantile(0.75)\n",
    "iqr = (high_cutoff_score - low_cutoff_score)\n",
    "outlier = iqr*1.5\n",
    "\n",
    "low = low_cutoff_score - outlier\n",
    "high = high_cutoff_score + outlier\n",
    "\n",
    "for num in range(df.shape[0]):\n",
    "  if (df['TotalScore'][num] >= high):\n",
    "    print(df['StudentNumber'][num], '학생 대단합니다!')\n",
    "  elif (df['TotalScore'][num] <= low):\n",
    "    print(df['StudentNumber'][num], '학생 할 수 있어요!')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.7.6 ('base')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.7.6"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "532ab19ce7265a7cb0ffcebe824f9b4866463c2fe53afda2435929c43d113303"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}