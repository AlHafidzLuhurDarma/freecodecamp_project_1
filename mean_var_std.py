def calculate(input):
  np_input = np.array(input)
  if len(np_input) != 9:
    raise ValueError('List must contain nine numbers.')
  input_format = np.array([[input[:3], input[3:6], input[6:9]]])

  mean_axis1 = np.mean(input_format, axis=1)
  mean_axis2 = np.mean(input_format, axis=2)
  mean = np.mean(input_format.flatten())

  variance_axis1 = np.var(input_format, axis=1)
  variance_axis2 = np.var(input_format, axis=2)
  variance = np.var(input_format.flatten())

  standard_deviation_axis1 = np.std(input_format, axis=1)
  standard_deviation_axis2 = np.std(input_format, axis=2)
  standard_deviation = np.std(input_format.flatten())

  max_axis1 = np.max(input_format, axis=1)
  max_axis2 = np.max(input_format, axis=2)
  max = np.max(input_format.flatten())

  min_axis1 = np.min(input_format, axis=1)
  min_axis2 = np.min(input_format, axis=2)
  min = np.min(input_format.flatten())

  sum_axis1 = np.sum(input_format, axis=1)
  sum_axis2 = np.sum(input_format, axis=2)
  sum = np.sum(input_format.flatten())

  mean_axis1 = mean_axis1.tolist()
  mean_axis2 = mean_axis2.tolist()
  mean = mean.tolist()

  variance_axis1 = variance_axis1.tolist()
  variance_axis2 = variance_axis2.tolist()
  variance = variance.tolist()

  standard_deviation_axis1 = standard_deviation_axis1.tolist()
  standard_deviation_axis2 = standard_deviation_axis2.tolist()
  standard_deviation = standard_deviation.tolist()

  max_axis1 = max_axis1.tolist()
  max_axis2 = max_axis2.tolist()
  max = max.tolist()

  min_axis1 = min_axis1.tolist()
  min_axis2 = min_axis2.tolist()
  min = min.tolist()

  sum_axis1 = sum_axis1.tolist()
  sum_axis2 = sum_axis2.tolist()
  sum = sum.tolist()

  result = {
    'mean': [mean_axis1, mean_axis2, mean],
    'variance': [variance_axis1, variance_axis2, variance],
    'standard deviation': [standard_deviation_axis1, standard_deviation_axis2, standard_deviation],
    'max': [max_axis1, max_axis2, max],
    'min': [min_axis1, min_axis2, min],
    'sum': [sum_axis1, sum_axis2, sum]
  }

  return result
