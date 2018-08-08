import csv
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='USERNAME', api_key='API_KEY')

#########COURT##########
court_shapes = []

#OUTER LINES#
outer_lines_shape = dict(
  type='rect',
  xref='x',
  yref='y',
  x0='-250',
  y0='-47.5',
  x1='250',
  y1='422.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1))
court_shapes.append(outer_lines_shape)

#HOOP#
hoop_shape = dict(
  type='circle',
  xref='x',
  yref='y',
  x0='7.5',
  y0='7.5',
  x1='-7.5',
  y1='-7.5',
  line=dict(
    color='rgba(10, 10, 10, 1)',
    width=1))
court_shapes.append(hoop_shape)

#Backboard#
backboard_shape = dict(
  type='rect',
  xref='x',
  yref='y',
  x0='-30',
  y0='-7.5',
  x1='30',
  y1='-6.5',
  line=dict(
    color='rgba(10, 10, 10, 1)',
    width=1),
  fillcolor='rgba(10, 10, 10, 1)')
court_shapes.append(backboard_shape)

#Outer Box 3-second Area#
outer_three_sec_shape = dict(
  type='rect',
  xref='x',
  yref='y',
  x0='-80',
  y0='-47.5',
  x1='80',
  y1='143.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1))
court_shapes.append(outer_three_sec_shape)

#Inner Box 3-second Area#
inner_three_sec_shape = dict(
  type='rect',
  xref='x',
  yref='y',
  x0='-60',
  y0='-47.5',
  x1='60',
  y1='143.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1))
court_shapes.append(inner_three_sec_shape)

####THREE POINT LINE####
#LEFT#
left_line_shape = dict(
  type='line',
  xref='x',
  yref='y',
  x0='-220',
  y0='-47.5',
  x1='-220',
  y1='92.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1))
court_shapes.append(left_line_shape)

#RIGHT#
right_line_shape = dict(
  type='line',
  xref='x',
  yref='y',
  x0='220',
  y0='-47.5',
  x1='220',
  y1='92.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1))
court_shapes.append(right_line_shape)

#ARC
three_point_arc_shape = dict(
  type='path',
  xref='x',
  yref='y',
  path='M -220 92.5 C -70 300, 70 300, 220 92.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1))
court_shapes.append(three_point_arc_shape)

#Center Circle#
center_circle_shape = dict(
  type='circle',
  xref='x',
  yref='y',
  x0='60',
  y0='482.5',
  x1='-60',
  y1='362.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1))
court_shapes.append(center_circle_shape)

#Restricted Circle#
res_circle_shape = dict(
  type='circle',
  xref='x',
  yref='y',
  x0='20',
  y0='442.5',
  x1='-20',
  y1='402.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1))
court_shapes.append(res_circle_shape)

#Free Throw Circle#
free_throw_circle_shape = dict(
  type='circle',
  xref='x',
  yref='y',
  x0='60',
  y0='200',
  x1='-60',
  y1='80',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1))
court_shapes.append(free_throw_circle_shape)

#Restricted Area#
res_area_shape = dict(
  type='circle',
  xref='x',
  yref='y',
  x0='40',
  y0='40',
  x1='-40',
  y1='-40',
  line=dict(
    color='rgba(10, 10, 10, 1)',
    width=1,
    dash='dot'))
court_shapes.append(res_area_shape)
