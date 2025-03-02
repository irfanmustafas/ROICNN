# Created by Zijing Mao at 2/10/2016

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import numpy as np

#region CONV_256_IDX
CONV_256_IDX = np.array([[1, 129, 2, 193, 65],
      [2, 1, 3, 193, 65],
      [3, 2, 4, 225, 33],
      [4, 3, 5, 247, 34],
      [5, 4, 6, 246, 35],
      [6, 5, 23, 7, 24],
      [7, 5, 8, 248, 6],
      [8, 7, 9, 249, 23],
      [9, 8, 10, 250, 22],
      [10, 9, 11, 251, 21],
      [11, 10, 12, 252, 20],
      [12, 11, 13, 253, 19],
      [13, 12, 14, 254, 18],
      [14, 13, 15, 255, 17],
      [15, 14, 0, 256, 16],
      [16, 17, 0, 15, 32],
      [17, 18, 16, 14, 31],
      [18, 19, 17, 13, 30],
      [19, 20, 18, 12, 29],
      [20, 21, 19, 11, 28],
      [21, 22, 20, 10, 27],
      [22, 23, 21, 9, 26],
      [23, 6, 22, 8, 25],
      [24, 5, 25, 6, 36],
      [25, 24, 26, 23, 37],
      [26, 25, 27, 22, 38],
      [27, 26, 28, 21, 39],
      [28, 27, 29, 20, 40],
      [29, 28, 30, 19, 41],
      [30, 29, 31, 18, 42],
      [31, 30, 32, 17, 43],
      [32, 31, 0, 16, 44],
      [33, 1, 34, 3, 66],
      [34, 33, 35, 4, 53],
      [35, 34, 36, 5, 54],
      [36, 35, 37, 24, 52],
      [37, 36, 38, 25, 51],
      [38, 37, 39, 26, 50],
      [39, 38, 40, 27, 49],
      [40, 39, 41, 28, 48],
      [41, 40, 42, 29, 47],
      [42, 41, 43, 30, 46],
      [43, 42, 44, 31, 45],
      [44, 43, 0, 32, 0],
      [45, 46, 0, 43, 62],
      [46, 47, 45, 42, 61],
      [47, 48, 46, 41, 60],
      [48, 49, 47, 40, 59],
      [49, 50, 48, 39, 58],
      [50, 51, 49, 38, 57],
      [51, 52, 57, 37, 56],
      [52, 53, 51, 36, 55],
      [53, 33, 54, 34, 67],
      [54, 53, 52, 35, 68],
      [55, 54, 56, 52, 69],
      [56, 55, 72, 51, 70],
      [57, 51, 58, 50, 72],
      [58, 57, 59, 49, 73],
      [59, 58, 60, 48, 74],
      [60, 59, 61, 47, 75],
      [61, 60, 62, 46, 76],
      [62, 61, 0, 45, 77],
      [63, 64, 0, 62, 0],
      [64, 75, 63, 61, 76],
      [65, 1, 66, 2, 97],
      [66, 65, 67, 33, 98],
      [67, 66, 68, 53, 89],
      [68, 67, 69, 54, 88],
      [69, 68, 70, 55, 87],
      [70, 69, 71, 56, 86],
      [71, 70, 79, 72, 85],
      [72, 56, 73, 57, 71],
      [73, 72, 74, 58, 79],
      [74, 73, 75, 59, 78],
      [75, 74, 64, 60, 77],
      [76, 77, 0, 64, 0],
      [77, 78, 76, 75, 81],
      [78, 79, 77, 74, 82],
      [79, 71, 78, 73, 84],
      [80, 84, 81, 78, 83],
      [81, 80, 0, 77, 82],
      [82, 83, 0, 81, 96],
      [83, 86, 82, 80, 95],
      [84, 85, 83, 79, 94],
      [85, 86, 84, 71, 93],
      [86, 87, 83, 70, 92],
      [87, 88, 86, 69, 91],
      [88, 89, 87, 68, 90],
      [89, 66, 88, 67, 99],
      [90, 89, 91, 88, 100],
      [91, 90, 92, 87, 101],
      [92, 91, 102, 86, 112],
      [93, 86, 94, 85, 102],
      [94, 93, 95, 84, 103],
      [95, 94, 96, 83, 104],
      [96, 95, 0, 82, 105],
      [97, 1, 130, 65, 161],
      [98, 97, 99, 66, 130],
      [99, 98, 100, 89, 131],
      [100, 99, 101, 90, 132],
      [101, 100, 112, 91, 113],
      [102, 92, 103, 93, 111],
      [103, 102, 104, 94, 110],
      [104, 103, 105, 95, 109],
      [105, 104, 106, 96, 108],
      [106, 105, 0, 0, 107],
      [107, 108, 0, 106, 119],
      [108, 109, 107, 105, 118],
      [109, 110, 108, 104, 117],
      [110, 111, 109, 103, 116],
      [111, 112, 110, 102, 115],
      [112, 101, 111, 92, 114],
      [113, 100, 114, 101, 133],
      [114, 113, 115, 112, 124],
      [115, 114, 116, 111, 123],
      [116, 115, 117, 110, 122],
      [117, 116, 118, 109, 121],
      [118, 117, 119, 108, 120],
      [119, 118, 0, 107, 0],
      [120, 121, 0, 118, 128],
      [121, 122, 120, 117, 127],
      [122, 123, 121, 116, 126],
      [123, 124, 122, 115, 125],
      [124, 133, 123, 114, 135],
      [125, 124, 126, 123, 136],
      [126, 125, 127, 122, 137],
      [127, 126, 128, 121, 138],
      [128, 127, 0, 120, 139],
      [129, 1, 146, 130, 162],
      [130, 97, 131, 98, 129],
      [131, 130, 132, 99, 148],
      [132, 131, 133, 100, 147],
      [133, 132, 124, 113, 134],
      [134, 147, 135, 133, 145],
      [135, 134, 136, 124, 144],
      [136, 135, 137, 125, 143],
      [137, 136, 138, 126, 142],
      [138, 137, 139, 127, 141],
      [139, 138, 140, 128, 140],
      [140, 141, 0, 139, 156],
      [141, 142, 140, 138, 155],
      [142, 143, 141, 137, 154],
      [143, 144, 142, 136, 153],
      [144, 145, 143, 135, 152],
      [145, 146, 144, 134, 151],
      [146, 129, 145, 147, 150],
      [147, 148, 134, 132, 146],
      [148, 129, 147, 131, 149],
      [149, 129, 150, 148, 163],
      [150, 149, 151, 146, 164],
      [151, 150, 152, 145, 165],
      [152, 151, 153, 144, 166],
      [153, 152, 154, 143, 160],
      [154, 153, 155, 142, 159],
      [155, 154, 156, 141, 158],
      [156, 155, 0, 140, 157],
      [157, 158, 0, 156, 170],
      [158, 159, 157, 155, 169],
      [159, 160, 158, 154, 168],
      [160, 152, 159, 153, 167],
      [161, 1, 162, 97, 193],
      [162, 161, 163, 129, 180],
      [163, 162, 164, 149, 179],
      [164, 163, 165, 150, 178],
      [165, 164, 166, 151, 177],
      [166, 165, 167, 152, 176],
      [167, 166, 168, 153, 175],
      [168, 167, 169, 154, 174],
      [169, 168, 170, 155, 173],
      [170, 169, 0, 156, 172],
      [171, 172, 0, 0, 189],
      [172, 173, 171, 170, 188],
      [173, 174, 172, 169, 187],
      [174, 175, 173, 168, 186],
      [175, 176, 174, 167, 185],
      [176, 177, 175, 166, 184],
      [177, 178, 176, 165, 183],
      [178, 179, 177, 164, 182],
      [179, 180, 178, 163, 181],
      [180, 161, 179, 162, 194],
      [181, 180, 196, 179, 195],
      [182, 181, 197, 178, 196],
      [183, 178, 184, 177, 197],
      [184, 183, 185, 176, 198],
      [185, 184, 186, 175, 199],
      [186, 185, 187, 174, 200],
      [187, 186, 188, 173, 192],
      [188, 187, 189, 172, 191],
      [189, 188, 0, 171, 203],
      [190, 191, 0, 189, 0],
      [191, 192, 190, 188, 202],
      [192, 200, 191, 187, 201],
      [193, 1, 194, 161, 2],
      [194, 193, 195, 180, 225],
      [195, 194, 228, 181, 226],
      [196, 181, 208, 182, 228],
      [197, 182, 198, 183, 208],
      [198, 197, 199, 184, 207],
      [199, 198, 200, 185, 206],
      [200, 199, 192, 186, 205],
      [201, 200, 202, 192, 204],
      [202, 201, 0, 191, 203],
      [203, 204, 0, 202, 213],
      [204, 205, 203, 201, 212],
      [205, 206, 204, 200, 211],
      [206, 207, 205, 199, 210],
      [207, 208, 206, 198, 209],
      [208, 196, 207, 197, 229],
      [209, 229, 218, 207, 231],
      [210, 207, 211, 206, 218],
      [211, 210, 212, 205, 217],
      [212, 211, 213, 204, 216],
      [213, 212, 0, 203, 215],
      [214, 215, 0, 0, 224],
      [215, 216, 214, 213, 222],
      [216, 217, 215, 212, 221],
      [217, 218, 216, 211, 220],
      [218, 209, 217, 210, 219],
      [219, 231, 220, 218, 232],
      [220, 219, 221, 217, 233],
      [221, 220, 222, 216, 234],
      [222, 221, 223, 215, 235],
      [223, 222, 224, 214, 236],
      [224, 223, 0, 0, 237],
      [225, 1, 226, 194, 3],
      [226, 225, 227, 195, 247],
      [227, 226, 230, 228, 246],
      [228, 195, 229, 196, 227],
      [229, 228, 209, 208, 230],
      [230, 227, 231, 202, 245],
      [231, 230, 219, 218, 232],
      [232, 244, 233, 219, 243],
      [233, 232, 234, 220, 242],
      [234, 233, 235, 221, 241],
      [235, 234, 236, 222, 240],
      [236, 235, 237, 223, 239],
      [237, 236, 0, 224, 238],
      [238, 239, 0, 237, 255],
      [239, 240, 238, 236, 254],
      [240, 241, 239, 235, 253],
      [241, 242, 240, 234, 252],
      [242, 243, 241, 233, 251],
      [243, 249, 242, 232, 250],
      [244, 245, 232, 231, 249],
      [245, 246, 244, 230, 248],
      [246, 247, 245, 227, 5],
      [247, 225, 246, 226, 4],
      [248, 246, 249, 245, 7],
      [249, 248, 250, 244, 8],
      [250, 249, 251, 243, 9],
      [251, 250, 252, 242, 10],
      [252, 251, 253, 241, 11],
      [253, 252, 254, 240, 12],
      [254, 253, 255, 239, 13],
      [255, 254, 256, 238, 14],
      [256, 255, 0, 0, 15]])
#endregion

#region CONV_128_IDX
CONV_128_IDX = np.array([[1, 87, 2, 111, 33], 
      [2, 1, 3, 111, 33], 
      [3, 2, 4, 112, 34], 
      [4, 3, 19, 113, 51], 
      [5, 4, 18, 6, 19], 
      [6, 113, 7, 124, 5], 
      [7, 6, 8, 123, 18], 
      [8, 7, 9, 125, 17], 
      [9, 8, 10, 126, 16], 
      [10, 9, 11, 127, 15], 
      [11, 10, 12, 128, 14], 
      [12, 11, 0, 0, 13], 
      [13, 14, 0, 12, 25], 
      [14, 15, 13, 11, 24], 
      [15, 16, 14, 10, 23], 
      [16, 17, 15, 9, 22], 
      [17, 18, 16, 8, 21], 
      [18, 5, 17, 7, 20], 
      [19, 4, 20, 5, 32], 
      [20, 19, 21, 18, 31], 
      [21, 20, 22, 17, 30], 
      [22, 21, 23, 16, 29], 
      [23, 22, 24, 15, 28], 
      [24, 23, 25, 14, 27], 
      [25, 24, 0, 13, 26], 
      [26, 27, 0, 25, 41], 
      [27, 28, 26, 24, 40], 
      [28, 29, 27, 23, 39], 
      [29, 30, 28, 22, 38], 
      [30, 31, 29, 21, 37], 
      [31, 32, 30, 20, 36], 
      [32, 4, 31, 19, 35], 
      [33, 1, 34, 2, 65], 
      [34, 33, 51, 3, 52], 
      [35, 51, 36, 32, 50], 
      [36, 35, 37, 31, 49], 
      [37, 36, 38, 30, 45], 
      [38, 37, 39, 29, 44], 
      [39, 38, 40, 28, 43], 
      [40, 39, 41, 27, 42], 
      [41, 40, 0, 26, 0], 
      [42, 43, 0, 40, 0], 
      [43, 44, 42, 39, 46], 
      [44, 45, 43, 38, 47], 
      [45, 36, 44, 37, 48], 
      [46, 47, 0, 43, 58], 
      [47, 48, 46, 44, 57], 
      [48, 49, 47, 45, 56], 
      [49, 50, 48, 36, 55], 
      [50, 51, 49, 35, 54], 
      [51, 34, 50, 4, 53], 
      [52, 33, 53, 34, 66], 
      [53, 52, 54, 51, 64], 
      [54, 53, 55, 50, 63], 
      [55, 54, 56, 49, 62], 
      [56, 55, 57, 48, 61], 
      [57, 56, 58, 47, 60], 
      [58, 57, 0, 46, 59], 
      [59, 60, 0, 58, 71], 
      [60, 61, 59, 57, 70], 
      [61, 62, 60, 56, 69], 
      [62, 63, 61, 55, 68], 
      [63, 64, 62, 54, 67], 
      [64, 66, 63, 53, 75], 
      [65, 1, 66, 33, 97], 
      [66, 65, 75, 52, 87], 
      [67, 75, 68, 63, 76], 
      [68, 67, 69, 62, 77], 
      [69, 68, 70, 61, 74], 
      [70, 69, 71, 60, 73], 
      [71, 72, 0, 59, 72], 
      [72, 73, 0, 71, 80], 
      [73, 74, 72, 70, 79], 
      [74, 68, 73, 69, 78], 
      [75, 66, 76, 64, 86], 
      [76, 75, 77, 67, 85], 
      [77, 76, 78, 68, 84], 
      [78, 77, 79, 74, 83], 
      [79, 78, 80, 73, 82], 
      [80, 79, 0, 72, 81], 
      [81, 82, 0, 80, 93], 
      [82, 83, 81, 79, 92], 
      [83, 84, 82, 78, 91], 
      [84, 85, 83, 77, 90], 
      [85, 86, 84, 76, 89], 
      [86, 87, 85, 75, 88], 
      [87, 1, 86, 66, 98], 
      [88, 98, 89, 86, 109], 
      [89, 88, 90, 85, 99], 
      [90, 89, 91, 84, 100], 
      [91, 90, 92, 83, 96], 
      [92, 91, 93, 82, 95], 
      [93, 92, 0, 81, 94], 
      [94, 95, 0, 93, 103], 
      [95, 96, 94, 92, 102], 
      [96, 90, 95, 91, 101], 
      [97, 1, 98, 65, 111], 
      [98, 97, 109, 87, 110], 
      [99, 109, 100, 89, 108], 
      [100, 99, 101, 90, 107], 
      [101, 100, 102, 96, 106], 
      [102, 101, 103, 95, 105], 
      [103, 102, 0, 94, 104], 
      [104, 105, 0, 103, 119], 
      [105, 106, 104, 102, 118], 
      [106, 107, 105, 101, 117], 
      [107, 108, 106, 100, 116], 
      [108, 109, 107, 99, 115], 
      [109, 98, 108, 88, 114], 
      [110, 111, 114, 98, 112], 
      [111, 1, 110, 97, 2], 
      [112, 111, 113, 110, 3], 
      [113, 112, 124, 114, 4], 
      [114, 110, 115, 109, 113], 
      [115, 114, 116, 108, 124], 
      [116, 115, 117, 107, 123], 
      [117, 116, 118, 106, 122], 
      [118, 117, 119, 105, 121], 
      [119, 118, 0, 104, 120], 
      [120, 121, 0, 119, 127], 
      [121, 122, 120, 118, 126], 
      [122, 123, 121, 117, 125], 
      [123, 124, 122, 116, 7], 
      [124, 113, 123, 115, 6], 
      [125, 123, 126, 122, 8], 
      [126, 125, 127, 121, 9], 
      [127, 126, 128, 120, 10], 
      [128, 127, 0, 0, 11]])
#endregion

#region CONV_64_IDX
CONV_64_IDX = np.array([[1, 0, 3, 2, 33], 
	[2, 1, 7, 0, 3], 
	[3, 1, 5, 2, 37], 
	[4, 33, 11, 5, 38], 
	[5, 3, 10, 6, 4], 
	[6, 1, 9, 7, 5], 
	[7, 2, 8, 0, 6], 
	[8, 7, 15, 0, 9], 
	[9, 6, 14, 8, 10], 
	[10, 5, 13, 9, 11], 
	[11, 4, 12, 10, 47], 
	[12, 11, 19, 13, 48], 
	[13, 10, 18, 14, 12], 
	[14, 9, 17, 15, 13], 
	[15, 8, 16, 0, 14], 
	[16, 15, 23, 0, 17], 
	[17, 14, 22, 16, 18], 
	[18, 13, 21, 17, 19], 
	[19, 12, 20, 18, 32], 
	[20, 19, 29, 21, 31], 
	[21, 18, 26, 22, 20], 
	[22, 17, 27, 23, 21], 
	[23, 16, 25, 24, 22], 
	[24, 0, 0, 0, 23], 
	[25, 23, 27, 0, 26], 
	[26, 21, 27, 25, 30], 
	[27, 26, 0, 25, 29], 
	[28, 29, 0, 0, 0], 
	[29, 30, 28, 27, 64], 
	[30, 31, 29, 26, 63], 
	[31, 32, 30, 20, 57], 
	[32, 48, 31, 19, 56], 
	[33, 0, 37, 1, 34], 
	[34, 0, 36, 33, 35], 
	[35, 34, 42, 36, 0], 
	[36, 34, 40, 37, 35], 
	[37, 33, 38, 3, 36], 
	[38, 37, 47, 4, 39], 
	[39, 33, 46, 38, 40], 
	[40, 36, 45, 39, 41], 
	[41, 34, 44, 40, 42], 
	[42, 35, 43, 41, 0], 
	[43, 42, 52, 44, 0], 
	[44, 41, 51, 45, 43], 
	[45, 40, 50, 46, 44], 
	[46, 39, 49, 47, 45], 
	[47, 38, 48, 11, 46], 
	[48, 47, 32, 12, 49], 
	[49, 46, 56, 48, 50], 
	[50, 45, 55, 49, 51], 
	[51, 44, 54, 50, 52], 
	[52, 43, 53, 51, 0], 
	[53, 52, 60, 54, 0], 
	[54, 51, 59, 55, 53], 
	[55, 50, 58, 56, 54], 
	[56, 49, 57, 32, 55], 
	[57, 56, 29, 31, 58], 
	[58, 55, 63, 57, 59], 
	[59, 54, 64, 58, 60], 
	[60, 53, 62, 59, 61], 
	[61, 0, 0, 60, 0], 
	[62, 60, 64, 63, 0], 
	[63, 58, 64, 30, 62], 
	[64, 63, 0, 29, 62]])
#endregion

#region CONV_32_IDX
CONV_32_IDX = np.array([[1, 0, 2, 3, 30], 
      [2, 1, 4, 0, 29], 
      [3, 1, 7, 0, 4], 
      [4, 2, 8, 3, 31], 
      [5, 0, 9, 6, 26], 
      [6, 1, 10, 0, 5], 
      [7, 3, 11, 0, 8], 
      [8, 4, 12, 7, 32], 
      [9, 5, 16, 10, 22], 
      [10, 6, 15, 0, 9], 
      [11, 7, 15, 0, 12], 
      [12, 8, 14, 11, 13], 
      [13, 32, 16, 12, 19], 
      [14, 12, 15, 0, 18], 
      [15, 14, 0, 11, 16], 
      [16, 13, 0, 15, 17], 
      [17, 18, 0, 16, 20], 
      [18, 19, 17, 14, 0], 
      [19, 23, 18, 13, 20], 
      [20, 24, 17, 19, 0], 
      [21, 25, 17, 22, 0], 
      [22, 26, 16, 9, 21], 
      [23, 27, 19, 32, 24], 
      [24, 28, 20, 23, 0], 
      [25, 30, 21, 26, 0], 
      [26, 0, 22, 5, 25], 
      [27, 29, 23, 31, 28], 
      [28, 30, 24, 27, 0], 
      [29, 30, 27, 2, 0], 
      [30, 0, 29, 1, 28], 
      [31, 0, 32, 4, 27], 
      [32, 31, 13, 8, 23]])
#endregion

#region CONV_16_IDX
CONV_16_IDX = np.array([[1, 0, 5, 6, 2], 
	[2, 0, 3, 1, 10], 
	[3, 2, 9, 4, 0], 
	[4, 0, 8, 5, 3], 
	[5, 1, 7, 0, 4], 
	[6, 1, 14, 0, 7], 
	[7, 5, 13, 6, 8], 
	[8, 4, 12, 7, 9], 
	[9, 3, 11, 8, 10], 
	[10, 2, 16, 9, 0], 
	[11, 9, 16, 12, 0], 
	[12, 8, 15, 13, 11], 
	[13, 7, 14, 0, 12], 
	[14, 13, 0, 6, 15], 
	[15, 12, 0, 14, 16], 
	[16, 11, 0, 15, 10]])
#endregion

#region CONV_8_IDX
CONV_8_IDX =  np.array([[1, 0, 3, 4, 2], 
	[2, 0, 3, 1, 5], 
	[3, 1, 5, 4, 2], 
	[4, 1, 7, 0, 3], 
	[5, 2, 8, 3, 0], 
	[6, 3, 7, 4, 8], 
	[7, 6, 0, 4, 8], 
	[8, 6, 0, 7, 5]])
#endregion

#region POOL_128_IDX
POOL_128_IDX = np.array([  [  1,  65],
                           [  2,   3],
                           [  3,   4],
                           [  5,   4],
                           [248,   7],
                           [245, 244],
                           [244, 232],
                           [243, 242],
                           [241, 242],
                           [240, 235],
                           [239, 238],
                           [238, 256],
                           [256,  15],
                           [254,  13],
                           [253,  12],
                           [252,  11],
                           [  9, 250],
                           [  8, 249],
                           [  6,   5],
                           [ 23,  22],
                           [ 22,  21],
                           [ 20,  21],
                           [ 19,  20],
                           [ 18,  17],
                           [ 17,  16],
                           [ 44,  32],
                           [ 42,  30],
                           [ 41,  29],
                           [ 40,  28],
                           [ 26,  38],
                           [ 25,  37],
                           [ 36,  24],
                           [ 65,  66],
                           [ 53,  33],
                           [ 52,  51],
                           [ 51,  57],
                           [ 50,  49],
                           [ 48,  49],
                           [ 47,  60],
                           [ 46,  45],
                           [ 45,  44],
                           [ 64,  62],
                           [ 75,  60],
                           [ 74,  73],
                           [ 57,  72],
                           [ 77,  81],
                           [ 78,  79],
                           [ 71,  79],
                           [ 70,  56],
                           [ 55,  69],
                           [ 54,  68],
                           [ 89,  66],
                           [ 88,  89],
                           [ 87,  88],
                           [ 86,  85],
                           [ 85,  93],
                           [ 83,  84],
                           [ 82,  83],
                           [105,  96],
                           [104, 103],
                           [102, 103],
                           [ 92, 112],
                           [101,  91],
                           [100,  99],
                           [ 97, 130],
                           [130, 131],
                           [113, 114],
                           [114, 115],
                           [115, 111],
                           [109, 110],
                           [108, 118],
                           [120, 118],
                           [121, 122],
                           [123, 122],
                           [132, 147],
                           [133, 134],
                           [135, 124],
                           [136, 125],
                           [127, 138],
                           [128, 139],
                           [140, 141],
                           [141, 142],
                           [143, 142],
                           [144, 143],
                           [145, 146],
                           [146, 148],
                           [129, 148],
                           [164, 150],
                           [165, 151],
                           [152, 166],
                           [153, 160],
                           [158, 155],
                           [157, 156],
                           [170, 172],
                           [169, 168],
                           [167, 168],
                           [161, 162],
                           [162, 163],
                           [177, 176],
                           [176, 175],
                           [175, 185],
                           [187, 186],
                           [188, 172],
                           [191, 202],
                           [192, 200],
                           [199, 200],
                           [198, 184],
                           [183, 197],
                           [178, 179],
                           [181, 180],
                           [193, 194],
                           [226, 225],
                           [227, 228],
                           [196, 181],
                           [208, 196],
                           [207, 206],
                           [206, 210],
                           [204, 205],
                           [203, 204],
                           [215, 213],
                           [216, 217],
                           [218, 217],
                           [209, 231],
                           [230, 229],
                           [232, 219],
                           [221, 220],
                           [222, 235],
                           [223, 237]])
#endregion

#region POOL_64_IDX
POOL_64_IDX = np.array([   [ 93,  92],
                           [ 94,  95],
                           [ 91,  92],
                           [ 89,  90],
                           [100,  96],
                           [102, 101],
                           [103, 102],
                           [104, 105],
                           [106, 105],
                           [108, 107],
                           [ 88, 109],
                           [110, 114],
                           [115, 114],
                           [117, 116],
                           [119, 118],
                           [120, 121],
                           [122, 121],
                           [124, 123],
                           [113, 112],
                           [  5,  18],
                           [  7,   8],
                           [126, 125],
                           [127, 126],
                           [128,  12],
                           [ 10,   9],
                           [ 17,  16],
                           [ 15,  16],
                           [ 25,  24],
                           [ 23,  22],
                           [ 21,  20],
                           [ 19,   4],
                           [  3,   2],
                           [ 81,  82],
                           [ 80,  79],
                           [ 72,  73],
                           [ 78,  79],
                           [ 83,  84],
                           [ 85,  86],
                           [ 76,  77],
                           [ 68,  74],
                           [ 70,  69],
                           [ 71,  70],
                           [ 59,  60],
                           [ 61,  60],
                           [ 63,  62],
                           [ 64,  75],
                           [ 87,  86],
                           [  1,   2],
                           [ 52,  53],
                           [ 54,  53],
                           [ 56,  55],
                           [ 58,  57],
                           [ 46,  47],
                           [ 48,  47],
                           [ 50,  49],
                           [ 51,  34],
                           [ 32,  31],
                           [ 36,  37],
                           [ 44,  45],
                           [ 43,  44],
                           [ 42,  41],
                           [ 39,  38],
                           [ 30,  29],
                           [ 28,  29]])
#endregion

#region POOL_32_IDX
POOL_32_IDX = np.array([   [ 1, 33],
                           [ 3,  5],
                           [ 7,  6],
                           [ 5,  4],
                           [11, 10],
                           [ 9,  6],
                           [15,  8],
                           [13, 10],
                           [19, 18],
                           [17, 22],
                           [23, 22],
                           [21, 20],
                           [31, 20],
                           [26, 21],
                           [27, 29],
                           [29, 27],
                           [64, 29],
                           [63, 58],
                           [58, 57],
                           [60, 59],
                           [54, 59],
                           [56, 55],
                           [50, 45],
                           [52, 43],
                           [44, 41],
                           [46, 45],
                           [40, 39],
                           [42, 41],
                           [36, 40],
                           [34, 33],
                           [38,  4],
                           [48, 12]])

#endregion

#region POOL_16_IDX
POOL_16_IDX = np.array([   [ 1,  2],
                           [30, 29],
                           [27, 29],
                           [31,  5],
                           [ 4,  2],
                           [ 7,  6],
                           [ 8,  5],
                           [32,  5],
                           [23, 22],
                           [24, 21],
                           [19, 18],
                           [13,  9],
                           [12, 14],
                           [15, 16],
                           [16, 15],
                           [17, 16]])
#endregion

#region POOL_8_IDX
POOL_8_IDX = np.array([   [ 1, 2],
                           [2, 1],
                           [4, 3],
                           [6, 7],
                           [10, 9],
                           [12, 11],
                           [14, 15],
                           [16, 15]])
#endregion

def roi_mapper_idx_select(chan_num, used_type='conv'):
    # which type to choose
    if used_type.lower() == 'conv':
        if chan_num == 256:
            chan_idx = CONV_256_IDX
        elif chan_num == 128:
            chan_idx = CONV_128_IDX
        elif chan_num == 64:
            chan_idx = CONV_64_IDX
        elif chan_num == 32:
            chan_idx = CONV_32_IDX
        elif chan_num == 16:
            chan_idx = CONV_16_IDX
        elif chan_num == 8:
            chan_idx = CONV_8_IDX
        else:
            print('Channel location not match, please make sure you used biosemi 265/128/64/32/16/8.')
            return
    elif used_type.lower() == 'pool':
        if chan_num == 128:
            chan_idx = POOL_128_IDX
        elif chan_num == 64:
            chan_idx = POOL_64_IDX
        elif chan_num == 32:
            chan_idx = POOL_32_IDX
        elif chan_num == 16:
            chan_idx = POOL_16_IDX
        elif chan_num == 8:
            chan_idx = POOL_8_IDX
        else:
            print('Channel location not match, please make sure you used biosemi 128/64/32/16/8.')
            return
    else:
        print('Used type not recognized, please type either conv/pool.')
        return

    return chan_idx
