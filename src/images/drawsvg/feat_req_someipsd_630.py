# Auto-generated from PySide6 Canvas to drawsvg
import drawsvg as draw

def _drawsvg_gradient(kind, coords, stops, attrs):
    if kind == 'linear':
        gradient = draw.LinearGradient(*coords, **attrs)
    else:
        cx, cy, radius, fx, fy, fr = coords
        gradient = draw.RadialGradient(cx, cy, radius, fx=fx, fy=fy, fr=fr, **attrs)
    for offset, color, alpha in stops:
        gradient.add_stop(offset, color, opacity=alpha)
    return gradient


def _drawsvg_effect(element, rect, shadow):
    dx, dy, radius, color, alpha = shadow
    x, y, width, height = rect
    # Qt uses a different blur kernel. Gaussian sigma=radius/2 is an
    # approximation; allow three sigma on every side to avoid clipping.
    margin = 1.5 * radius
    left = min(x, x + dx) - margin
    top = min(y, y + dy) - margin
    right = max(x + width, x + width + dx) + margin
    bottom = max(y + height, y + height + dy) + margin
    effect = draw.Filter(x=left, y=top, width=max(1, right-left),
                         height=max(1, bottom-top), filterUnits='userSpaceOnUse',
                         primitiveUnits='userSpaceOnUse', color_interpolation_filters='sRGB')
    if radius > 0:
        effect.append(draw.FilterItem('feGaussianBlur', in_='SourceAlpha',
                                     stdDeviation=radius/2, result='shadow-alpha'))
    effect.append(draw.FilterItem('feOffset', in_='shadow-alpha' if radius > 0 else 'SourceAlpha',
                                 dx=dx, dy=dy, result='shadow-offset'))
    effect.append(draw.FilterItem('feFlood', flood_color=color, flood_opacity=alpha,
                                 result='shadow-color'))
    effect.append(draw.FilterItem('feComposite', in_='shadow-color', in2='shadow-offset',
                                 operator='in', result='shadow'))
    merge = draw.FilterItem('feMerge')
    merge.append(draw.FilterItem('feMergeNode', in_='shadow'))
    merge.append(draw.FilterItem('feMergeNode', in_='SourceGraphic'))
    effect.append(merge)
    # Qt shadow offset/radius use device coordinates. Apply the filter outside
    # the item's transform so rotations and scaling do not change those values.
    transform = element.args.pop('transform', None)
    source = draw.Group(transform=transform) if transform else draw.Group()
    source.append(element)
    result = draw.Group(filter=effect)
    result.append(source)
    return result

def build_drawing():
    d = draw.Drawing(1022.0, 631.0, origin=(-1172.8503937007874, -257.2598425196851), viewBox='-1172.8503937007874 -257.2598425196851 1022.0 631.0')
    d.append(draw.Rectangle(-1172.8503937007874, -257.2598425196851, 1022.0, 631.0, fill='white', stroke='none'))

    _rect = draw.Rectangle(0.00, 0.00, 1010.00, 570.00, fill='#f9c499', fill_opacity=0.392156869173, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, data_label_id='rect_label_1', rx=8.76, ry=8.76, transform='matrix(1.000000 0.000000 0.000000 1.000000 -1166.850394 -251.259843)')
    d.append(_rect)
    # Multiline label for rect_label_1
    _rect_label = draw.Text("SD Client State Machine (Services)", 19.00, 497.00, 17.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.105263, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_1', data_label_h='center', data_label_v='top', data_font_px=19.0000, data_raw_label='SD Client State Machine (Services)', data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1158.850394 -243.259843)')
    _rect_label.escaped_text = ''
    _rect_label.children.clear()
    _rect_label.append_line('SD Client State Machine (Services)', x=346.0000, y=17.0000, direction='ltr', text_anchor='start')
    d.append(_rect_label)

    _rect = draw.Rectangle(0.00, 0.00, 440.00, 450.00, fill='#c2ff80', fill_opacity=0.392156869173, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, data_label_id='rect_label_2', rx=9.00, ry=9.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -606.850394 -141.259843)')
    d.append(_rect)
    # Multiline label for rect_label_2
    _rect_label = draw.Text("Ready", 16.00, 212.00, 14.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.125000, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_2', data_label_h='center', data_label_v='top', data_font_px=16.0000, data_raw_label='Ready', data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -598.850394 -133.259843)')
    _rect_label.escaped_text = ''
    _rect_label.children.clear()
    _rect_label.append_line('Ready', x=189.5000, y=14.0000, direction='ltr', text_anchor='start')
    d.append(_rect_label)

    _rect = draw.Rectangle(0.00, 0.00, 410.00, 140.00, fill='#ffffff', fill_opacity=0, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, data_label_id='rect_label_3', rx=8.76, ry=8.76, transform='matrix(1.000000 0.000000 0.000000 1.000000 -586.850394 148.740157)')
    d.append(_rect)
    # Multiline label for rect_label_3
    _rect_label = draw.Text("Main Phase", 12.00, 197.00, 11.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_3', data_label_h='center', data_label_v='top', data_font_px=12.0000, data_raw_label='Main Phase', data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -578.850394 156.740157)')
    _rect_label.escaped_text = ''
    _rect_label.children.clear()
    _rect_label.append_line('Main Phase', x=164.5000, y=11.0000, direction='ltr', text_anchor='start')
    d.append(_rect_label)

    _rect = draw.Rectangle(0.00, 0.00, 370.00, 120.00, fill='#ffffff', fill_opacity=0, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, data_label_id='rect_label_4', rx=7.20, ry=7.20, transform='matrix(1.000000 0.000000 0.000000 1.000000 -546.850394 -1.259843)')
    d.append(_rect)
    # Multiline label for rect_label_4
    _rect_label = draw.Text("Repetition Phase", 12.00, 177.00, 11.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_4', data_label_h='center', data_label_v='top', data_font_px=12.0000, data_raw_label='Repetition Phase', data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -538.850394 6.740157)')
    _rect_label.escaped_text = ''
    _rect_label.children.clear()
    _rect_label.append_line('Repetition Phase', x=129.5000, y=11.0000, direction='ltr', text_anchor='start')
    d.append(_rect_label)

    _rect = draw.Rectangle(0.00, 0.00, 370.00, 90.00, fill='#ffffff', fill_opacity=0, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, data_label_id='rect_label_5', rx=6.44, ry=6.44, transform='matrix(1.000000 0.000000 0.000000 1.000000 -546.850394 -111.259843)')
    d.append(_rect)
    # Multiline label for rect_label_5
    _rect_label = draw.Text("Initial Wait Phase", 12.00, 177.00, 11.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_5', data_label_h='center', data_label_v='top', data_font_px=12.0000, data_raw_label='Initial Wait Phase', data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -538.850394 -103.259843)')
    _rect_label.escaped_text = ''
    _rect_label.children.clear()
    _rect_label.append_line('Initial Wait Phase', x=129.5000, y=11.0000, direction='ltr', text_anchor='start')
    d.append(_rect_label)

    _rect = draw.Rectangle(0.00, 0.00, 290.00, 320.00, fill='#c6c2bc', fill_opacity=0.392156869173, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, data_label_id='rect_label_6', rx=8.70, ry=8.70, transform='matrix(1.000000 0.000000 0.000000 1.000000 -1156.850394 -141.259843)')
    d.append(_rect)
    # Multiline label for rect_label_6
    _rect_label = draw.Text("Not Requested", 16.00, 137.00, 14.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.125000, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_6', data_label_h='center', data_label_v='top', data_font_px=16.0000, data_raw_label='Not Requested', data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1148.850394 -133.259843)')
    _rect_label.escaped_text = ''
    _rect_label.children.clear()
    _rect_label.append_line('Not Requested', x=85.0000, y=14.0000, direction='ltr', text_anchor='start')
    d.append(_rect_label)

    _rect = draw.Rectangle(0.00, 0.00, 110.00, 40.00, fill='#ffffff', fill_opacity=0, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, data_label_id='rect_label_7', rx=9.00, ry=9.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -296.850394 38.740157)')
    d.append(_rect)
    # Multiline label for rect_label_7
    _rect_label = draw.Text("Timer Set", 12.00, 47.00, 11.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_7', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_raw_label='Timer Set', data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -288.850394 51.740157)')
    _rect_label.escaped_text = ''
    _rect_label.children.clear()
    _rect_label.append_line('Timer Set', x=20.5000, y=11.0000, direction='ltr', text_anchor='start')
    d.append(_rect_label)

    _rect = draw.Rectangle(0.00, 0.00, 110.00, 40.00, fill='#ffffff', fill_opacity=0, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, data_label_id='rect_label_8', rx=9.00, ry=9.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -296.850394 -91.259843)')
    d.append(_rect)
    # Multiline label for rect_label_8
    _rect_label = draw.Text("Timer Set", 12.00, 47.00, 11.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_8', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_raw_label='Timer Set', data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -288.850394 -78.259843)')
    _rect_label.escaped_text = ''
    _rect_label.children.clear()
    _rect_label.append_line('Timer Set', x=20.5000, y=11.0000, direction='ltr', text_anchor='start')
    d.append(_rect_label)

    _text = draw.Text(["RBD = REPETITION_BASE_DELAY", "REP_MAX = REPETITION_MAX"], 10.67, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.125000, xml__space='preserve', data_doc_margin=4.0000, data_font_px=10.6667, data_scale=1.000000, data_raw_text='RBD = REPETITION_BASE_DELAY&#10;REP_MAX = REPETITION_MAX', data_box_w=171.0000, data_box_h=50.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1166.850394 318.740157)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('RBD = REPETITION_BASE_DELAY', x=4.0000, y=14.0000, direction='ltr', text_anchor='start')
    _text.append_line('REP_MAX = REPETITION_MAX', x=4.0000, y=26.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _path = draw.Path('M 30.00 -10.00 L 30.00 80.00', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -556.850394 68.740157)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M 30.00 80.00 L 25.00 70.00 L 35.00 70.00 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(1.000000 0.000000 0.000000 1.000000 -556.850394 68.740157)')
    d.append(_arrow_head)
    d.append(_path)

    _rect = draw.Rectangle(0.00, 0.00, 210.00, 40.00, fill='none', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, data_label_id='rect_label_9', rx=9.00, ry=9.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -1096.850394 78.740157)')
    d.append(_rect)
    # Multiline label for rect_label_9
    _rect_label = draw.Text("Service Seen", 12.00, 97.00, 11.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_9', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_raw_label='Service Seen', data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1088.850394 91.740157)')
    _rect_label.escaped_text = ''
    _rect_label.children.clear()
    _rect_label.append_line('Service Seen', x=61.0000, y=11.0000, direction='ltr', text_anchor='start')
    d.append(_rect_label)

    _rect = draw.Rectangle(0.00, 0.00, 110.00, 40.00, fill='#000000', fill_opacity=0, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, data_label_id='rect_label_10', rx=8.00, ry=8.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -296.850394 198.740157)')
    d.append(_rect)
    # Multiline label for rect_label_10
    _rect_label = draw.Text("Stopped", 12.00, 47.00, 11.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_10', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_raw_label='Stopped', data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -288.850394 211.740157)')
    _rect_label.escaped_text = ''
    _rect_label.children.clear()
    _rect_label.append_line('Stopped', x=24.0000, y=11.0000, direction='ltr', text_anchor='start')
    d.append(_rect_label)

    _rect = draw.Rectangle(0.00, 0.00, 100.00, 40.00, fill='#ffffff', fill_opacity=0, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, data_label_id='rect_label_11', rx=9.00, ry=9.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -536.850394 198.740157)')
    d.append(_rect)
    # Multiline label for rect_label_11
    _rect_label = draw.Text("Service Ready", 12.00, 42.00, 11.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_11', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_raw_label='Service Ready', data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -528.850394 211.740157)')
    _rect_label.escaped_text = ''
    _rect_label.children.clear()
    _rect_label.append_line('Service Ready', x=3.0000, y=11.0000, direction='ltr', text_anchor='start')
    d.append(_rect_label)

    _text = draw.Text(["[run<REP_MAX]", "/send(FindService) ", "run++", "setTimer((2^run)*RBD)"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='[run&lt;REP_MAX]&#10;/send(FindService) &#10;run++&#10;setTimer((2^run)*RBD)', data_box_w=120.0000, data_box_h=50.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -376.850394 68.740157)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('[run<REP_MAX]', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('/send(FindService) ', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    _text.append_line('run++', x=4.0000, y=32.0000, direction='ltr', text_anchor='start')
    _text.append_line('setTimer((2^run)*RBD)', x=4.0000, y=42.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text("[REP_MAX==0]", 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='[REP_MAX==0]', data_box_w=80.0000, data_box_h=20.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -526.850394 118.740157)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('[REP_MAX==0]', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text("[ServiceNot Requested]", 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='[ServiceNot Requested]', data_box_w=110.0000, data_box_h=20.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1006.850394 -181.259843)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('[ServiceNot Requested]', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text(["[ServiceRequested and", "ifstatus!=up_and_configured]"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='[ServiceRequested and&#10;ifstatus!=up_and_configured]', data_box_w=140.0000, data_box_h=30.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -736.850394 -181.259843)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('[ServiceRequested and', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('ifstatus!=up_and_configured]', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text("Initial", 9.33, 0.00, 0.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=0.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='Initial', data_box_w=40.0000, data_box_h=10.0000, data_auto_size=False, data_text_h='center', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -756.850394 -211.259843)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('Initial', x=9.0000, y=8.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text("Initial", 9.33, 0.00, 0.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=0.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='Initial', data_box_w=40.0000, data_box_h=10.0000, data_auto_size=False, data_text_h='center', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -596.850394 -91.259843)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('Initial', x=9.0000, y=8.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text("Initial", 9.33, 0.00, 0.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=0.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='Initial', data_box_w=40.0000, data_box_h=10.0000, data_auto_size=False, data_text_h='center', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -546.850394 -91.259843)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('Initial', x=9.0000, y=8.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text("Initial", 9.33, 0.00, 0.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=0.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='Initial', data_box_w=40.0000, data_box_h=10.0000, data_auto_size=False, data_text_h='center', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -546.850394 38.740157)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('Initial', x=9.0000, y=8.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text("Initial", 9.33, 0.00, 0.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=0.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='Initial', data_box_w=40.0000, data_box_h=10.0000, data_auto_size=False, data_text_h='center', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1146.850394 -101.259843)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('Initial', x=9.0000, y=8.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text("Initial", 9.33, 0.00, 0.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=0.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='Initial', data_box_w=40.0000, data_box_h=10.0000, data_auto_size=False, data_text_h='center', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -546.850394 158.740157)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('Initial', x=9.0000, y=8.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text(["InternalServiceRequest", "[ifstatus==up_and_configured]"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='InternalServiceRequest&#10;[ifstatus==up_and_configured]', data_box_w=160.0000, data_box_h=30.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -896.850394 228.740157)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('InternalServiceRequest', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('[ifstatus==up_and_configured]', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text(["InternalServiceRelease", "[ServiceNotRequested]"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='InternalServiceRelease&#10;[ServiceNotRequested]', data_box_w=130.0000, data_box_h=30.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -896.850394 178.740157)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('InternalServiceRelease', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('[ServiceNotRequested]', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text(["InternalServiceRelease", "[ServiceNotRequested]"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='InternalServiceRelease&#10;[ServiceNotRequested]', data_box_w=130.0000, data_box_h=30.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -896.850394 268.740157)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('InternalServiceRelease', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('[ServiceNotRequested]', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _path = draw.Path('M -601.85 -532.30 L -601.85 -392.30', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -475.000394 471.036269)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -601.85 -392.30 L -606.85 -402.30 L -596.85 -402.30 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(1.000000 0.000000 0.000000 1.000000 -475.000394 471.036269)')
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["Timer ", "expired ", "(TTL)"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='Timer expired (TTL)', data_box_w=40.0000, data_box_h=40.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1056.850394 -51.259843)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('Timer ', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('expired ', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    _text.append_line('(TTL)', x=4.0000, y=32.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _path = draw.Path('M -381.19 -533.14 L -381.19 -553.14 L -411.19 -553.14 L -411.19 -533.14', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(-1.000000 0.000000 -0.000000 -1.000000 -1398.044062 -414.404114)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -411.19 -533.14 L -416.19 -543.14 L -406.19 -543.14 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(-1.000000 0.000000 -0.000000 -1.000000 -1398.044062 -414.404114)')
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["receive(Offer", "Service)", "/setTimer(TTL)"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='receive(OfferService)&#10;/setTimer(TTL)', data_box_w=70.0000, data_box_h=60.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1146.850394 -31.259843)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('receive(Offer', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('Service)', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    _text.append_line('/setTimer(TTL)', x=4.0000, y=32.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text(["receive(OfferService)", "/resetTimer(TTL)"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='receive(OfferService)&#10;/resetTimer(TTL)', data_box_w=110.0000, data_box_h=30.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1076.850394 138.740157)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('receive(OfferService)', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('/resetTimer(TTL)', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text(["receive", "(StopOffer", "Servicer)/", "cancelTimer", "(TTL)"], 9.33, 3.00, 3.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=3.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='receive&#10;(StopOffer&#10;Servicer)/&#10;cancelTimer&#10;(TTL)', data_box_w=60.0000, data_box_h=70.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1016.850394 -21.259843)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('receive', x=3.0000, y=11.0000, direction='ltr', text_anchor='start')
    _text.append_line('(StopOffer', x=3.0000, y=21.0000, direction='ltr', text_anchor='start')
    _text.append_line('Servicer)/', x=3.0000, y=31.0000, direction='ltr', text_anchor='start')
    _text.append_line('cancelTimer', x=3.0000, y=41.0000, direction='ltr', text_anchor='start')
    _text.append_line('(TTL)', x=3.0000, y=51.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text(["if-status-changed() ", "[ifstatus!", "=up_and_configured]", "/cancelTimer(TTL)"], 9.33, 3.00, 3.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=3.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='if-status-changed() [ifstatus!&#10;=up_and_configured]&#10;/cancelTimer(TTL)', data_box_w=100.0000, data_box_h=60.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -956.850394 28.740157)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('if-status-changed() ', x=3.0000, y=11.0000, direction='ltr', text_anchor='start')
    _text.append_line('[ifstatus!', x=3.0000, y=21.0000, direction='ltr', text_anchor='start')
    _text.append_line('=up_and_configured]', x=3.0000, y=31.0000, direction='ltr', text_anchor='start')
    _text.append_line('/cancelTimer(TTL)', x=3.0000, y=41.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _rect = draw.Rectangle(0.00, 0.00, 210.00, 40.00, fill='none', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, data_label_id='rect_label_12', rx=9.00, ry=9.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -1096.850394 -101.259843)')
    d.append(_rect)
    # Multiline label for rect_label_12
    _rect_label = draw.Text("Service Not Seen", 12.00, 97.00, 11.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_12', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_raw_label='Service Not Seen', data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1088.850394 -88.259843)')
    _rect_label.escaped_text = ''
    _rect_label.children.clear()
    _rect_label.append_line('Service Not Seen', x=50.0000, y=11.0000, direction='ltr', text_anchor='start')
    d.append(_rect_label)

    _path = draw.Path('M -1006.13 -587.32 L -1146.13 -587.32', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(0.000000 1.000000 -1.000000 0.000000 -1644.166122 1084.867432)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1146.13 -587.32 L -1136.13 -592.32 L -1136.13 -582.32 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(0.000000 1.000000 -1.000000 0.000000 -1644.166122 1084.867432)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -917.22 -404.12 L -1057.22 -404.12', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(0.000000 1.000000 -1.000000 0.000000 -1360.973204 995.961883)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1057.22 -404.12 L -1047.22 -409.12 L -1047.22 -399.12 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(0.000000 1.000000 -1.000000 0.000000 -1360.973204 995.961883)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -1001.38 -596.73 L -1141.38 -596.73', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(0.000000 1.000000 -1.000000 0.000000 -1613.582530 1080.118022)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1141.38 -596.73 L -1131.38 -601.73 L -1131.38 -591.73 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(0.000000 1.000000 -1.000000 0.000000 -1613.582530 1080.118022)')
    d.append(_arrow_head)
    d.append(_path)

    _circ = draw.Circle(10.00, 10.00, 10.00, fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, transform='matrix(0.909259 0.000000 0.000000 0.909259 -1136.850394 -91.259843)')
    d.append(_circ)

    _path = draw.Path('M -853.97 -53.23 L -886.96 -53.23', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=True, data_arrow_end=False, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(0.909259 0.000000 0.000000 0.909259 -320.373352 -32.857954)')
    # Arrowheads: start=true, end=false, length=10.00, width=10.00
    _arrow_head = draw.Path('M -853.97 -53.23 L -863.97 -48.23 L -863.97 -58.23 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(0.909259 0.000000 0.000000 0.909259 -320.373352 -32.857954)')
    d.append(_arrow_head)
    d.append(_path)

    _rect = draw.Rectangle(0.00, 0.00, 80.00, 320.00, fill='#b34f2e', fill_opacity=0.392156869173, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, data_label_id='rect_label_13', rx=9.00, ry=9.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -776.850394 -141.259843)')
    d.append(_rect)
    # Multiline label for rect_label_13
    _rect_label = draw.Text(["Requested ", "but not ", "Ready"], 12.00, 32.00, 11.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_13', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_raw_label='Requested but not Ready', data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -768.850394 -1.259843)')
    _rect_label.escaped_text = ''
    _rect_label.children.clear()
    _rect_label.append_line('Requested ', x=1.5000, y=11.0000, direction='ltr', text_anchor='start')
    _rect_label.append_line('but not ', x=13.5000, y=24.0000, direction='ltr', text_anchor='start')
    _rect_label.append_line('Ready', x=14.5000, y=37.0000, direction='ltr', text_anchor='start')
    d.append(_rect_label)

    _text = draw.Text(["InternalService", "Request", "[ifstatus!=up_and_", "configured]", "/cancelTimer(TTL)"], 9.33, 2.00, 2.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=2.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='InternalService&#10;Request&#10;[ifstatus!=up_and_&#10;configured]&#10;/cancelTimer(TTL)', data_box_w=90.0000, data_box_h=60.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -866.850394 -41.259843)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('InternalService', x=2.0000, y=10.0000, direction='ltr', text_anchor='start')
    _text.append_line('Request', x=2.0000, y=20.0000, direction='ltr', text_anchor='start')
    _text.append_line('[ifstatus!=up_and_', x=2.0000, y=30.0000, direction='ltr', text_anchor='start')
    _text.append_line('configured]', x=2.0000, y=40.0000, direction='ltr', text_anchor='start')
    _text.append_line('/cancelTimer(TTL)', x=2.0000, y=50.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _path = draw.Path('M -644.25 -138.22 L -734.25 -138.22', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=True, data_arrow_end=False, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 37.397350 146.962822)')
    # Arrowheads: start=true, end=false, length=10.00, width=10.00
    _arrow_head = draw.Path('M -644.25 -138.22 L -654.25 -133.22 L -654.25 -143.22 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(1.000000 0.000000 0.000000 1.000000 37.397350 146.962822)')
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["if-status-changed()", "[ifstatus!", "=up_and_configured]", "/cancelTimer(TTL)"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='if-status-changed()&#10;[ifstatus!&#10;=up_and_configured]&#10;/cancelTimer(TTL)', data_box_w=100.0000, data_box_h=50.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -696.850394 28.740157)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('if-status-changed()', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('[ifstatus!', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    _text.append_line('=up_and_configured]', x=4.0000, y=32.0000, direction='ltr', text_anchor='start')
    _text.append_line('/cancelTimer(TTL)', x=4.0000, y=42.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text(["if-status-changed()", "[ifstatus==up_and_", "configured]"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='if-status-changed()&#10;[ifstatus==up_and_configured]', data_box_w=90.0000, data_box_h=40.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -696.850394 -31.259843)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('if-status-changed()', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('[ifstatus==up_and_', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    _text.append_line('configured]', x=4.0000, y=32.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _circ = draw.Circle(10.00, 10.00, 10.00, fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=0.70, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, transform='matrix(1.000000 0.000000 0.000000 1.000000 -746.850394 -201.259843)')
    d.append(_circ)

    _path = draw.Path('M -30.83 -1.96 L 59.17 -1.96', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=True, data_arrow_end=False, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -666.021696 30.701052)')
    # Arrowheads: start=true, end=false, length=10.00, width=10.00
    _arrow_head = draw.Path('M -30.83 -1.96 L -20.83 -6.96 L -20.83 3.04 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(1.000000 0.000000 0.000000 1.000000 -666.021696 30.701052)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -20.83 -1.96 L 69.17 -1.96', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -846.021696 20.701052)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M 69.17 -1.96 L 59.17 3.04 L 59.17 -6.96 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(1.000000 0.000000 0.000000 1.000000 -846.021696 20.701052)')
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["receive(OfferService)", "/setTimer(TTL)"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='receive(OfferService)&#10;/setTimer(TTL)', data_box_w=100.0000, data_box_h=30.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -386.850394 118.740157)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('receive(OfferService)', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('/setTimer(TTL)', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text(["[REP_MAX>0]", "/run=0", "setTimer((2^run)*RBD)"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='[REP_MAX&gt;0]&#10;/run=0&#10;setTimer((2^run)*RBD)', data_box_w=110.0000, data_box_h=40.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -486.850394 18.740157)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('[REP_MAX>0]', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('/run=0', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    _text.append_line('setTimer((2^run)*RBD)', x=4.0000, y=32.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text(["/setTimerInRange(INITIAL_DELAY_MIN,", "INITIAL_DELAY_MAX)"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='/setTimerInRange(INITIAL_DELAY_MIN,&#10;INITIAL_DELAY_MAX)', data_box_w=180.0000, data_box_h=30.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -506.850394 -71.259843)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('/setTimerInRange(INITIAL_DELAY_MIN,', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('INITIAL_DELAY_MAX)', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _circ = draw.Circle(10.00, 10.00, 10.00, fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, transform='matrix(0.909259 0.000000 0.000000 0.909259 -536.850394 168.740157)')
    d.append(_circ)

    _circ = draw.Circle(10.00, 10.00, 10.00, fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, transform='matrix(0.909259 0.000000 0.000000 0.909259 -586.850394 -81.259843)')
    d.append(_circ)

    _path = draw.Path('M -751.10 -158.48 L -751.10 -128.48', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 354.251444 277.218460)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -751.10 -128.48 L -756.10 -138.48 L -746.10 -138.48 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(1.000000 0.000000 0.000000 1.000000 354.251444 277.218460)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -778.85 88.74 L -778.85 110.74 L -745.85 110.74 L -745.85 88.74', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(0.909259 0.000000 0.000000 0.909259 421.322477 -1.947509)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -745.85 88.74 L -740.85 98.74 L -750.85 98.74 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(0.909259 0.000000 0.000000 0.909259 421.322477 -1.947509)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -1031.15 -73.10 L -987.16 -73.10 L -987.16 -51.10', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(0.909259 0.000000 0.000000 0.909259 410.730374 245.203820)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -987.16 -51.10 L -992.16 -61.10 L -982.16 -61.10 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(0.909259 0.000000 0.000000 0.909259 410.730374 245.203820)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -1075.14 -62.10 L -1042.15 -62.10', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(0.909259 0.000000 0.000000 0.909259 400.730374 -14.796180)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1042.15 -62.10 L -1052.15 -57.10 L -1052.15 -67.10 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(0.909259 0.000000 0.000000 0.909259 400.730374 -14.796180)')
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["receive(OfferService)", "/resetTimer(TTL)"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='receive(OfferService)&#10;/resetTimer(TTL)', data_box_w=100.0000, data_box_h=30.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -526.850394 258.740157)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('receive(OfferService)', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('/resetTimer(TTL)', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text(["Timer ", "expired(TTL)"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='Timer expired(TTL)', data_box_w=60.0000, data_box_h=30.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -686.850394 168.740157)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('Timer ', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('expired(TTL)', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text(["Timer Expired", "/send(FindService)"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='Timer Expired&#10;/send(FindService)', data_box_w=90.0000, data_box_h=30.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -296.850394 -51.259843)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('Timer Expired', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('/send(FindService)', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text(["Timer Expired", "[run>=REP_MAX]", " "], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='Timer Expired&#10;[run&gt;=REP_MAX]&#10;', data_box_w=80.0000, data_box_h=30.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -246.850394 118.740157)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('Timer Expired', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('[run>=REP_MAX]', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    _text.append_line('', x=4.0000, y=32.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _path = draw.Path('M -524.83 -241.88 L -664.83 -241.88', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 227.974744 470.618800)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -664.83 -241.88 L -654.83 -246.88 L -654.83 -236.88 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(1.000000 0.000000 0.000000 1.000000 227.974744 470.618800)')
    d.append(_arrow_head)
    d.append(_path)

    _circ = draw.Circle(10.00, 10.00, 10.00, fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, transform='matrix(1.000185 0.000000 0.000000 1.000185 -536.850394 48.740157)')
    d.append(_circ)

    _path = draw.Path('M -805.18 -24.23 L -805.18 107.75', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(0.909259 0.000000 0.000000 0.909259 485.269495 100.771676)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -805.18 107.75 L -810.18 97.75 L -800.18 97.75 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(0.909259 0.000000 0.000000 0.909259 485.269495 100.771676)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -805.18 -13.23 L -805.18 41.76', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(0.909259 0.000000 0.000000 0.909259 525.269495 -39.228324)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -805.18 41.76 L -810.18 31.76 L -800.18 31.76 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(0.909259 0.000000 0.000000 0.909259 525.269495 -39.228324)')
    d.append(_arrow_head)
    d.append(_path)

    _circ = draw.Circle(10.00, 10.00, 10.00, fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, transform='matrix(0.909259 0.000000 0.000000 0.909259 -536.850394 -81.259843)')
    d.append(_circ)

    _path = draw.Path('M -1083.76 177.14 L -843.76 177.14 L -843.76 227.14', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 466.908107 -368.398314)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -843.76 227.14 L -848.76 217.14 L -838.76 217.14 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(1.000000 0.000000 0.000000 1.000000 466.908107 -368.398314)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -1027.81 68.74 L -785.85 68.74', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(0.909259 0.000000 0.000000 0.909259 417.692847 -3.762324)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -785.85 68.74 L -795.85 73.74 L -795.85 63.74 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(0.909259 0.000000 0.000000 0.909259 417.692847 -3.762324)')
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["[ServiceRequested and", "ifstatus==up_and_configured]"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='[ServiceRequested and&#10;ifstatus==up_and_configured]', data_box_w=140.0000, data_box_h=30.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -506.850394 -181.259843)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('[ServiceRequested and', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('ifstatus==up_and_configured]', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text(["receive(OfferService)", "/setTimer(TTL)"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='receive(OfferService)&#10;/setTimer(TTL)', data_box_w=110.0000, data_box_h=30.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -416.850394 228.740157)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('receive(OfferService)', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('/setTimer(TTL)', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _text = draw.Text(["receive(StopOfferService)", "/cancelTimer(TTL)"], 9.33, 4.00, 4.00, fill='#000000', opacity=1.000000, font_family='Arial', font_weight='normal', font_style='normal', text_decoration='none', data_xml_escaped='true', text_anchor='start', dominant_baseline='alphabetic', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text='receive(StopOfferService)&#10;/cancelTimer(TTL)', data_box_w=120.0000, data_box_h=30.0000, data_auto_size=False, data_text_h='left', data_text_v='top', data_text_dir='ltr', direction='ltr', unicode_bidi='embed', transform='matrix(1.000000 0.000000 0.000000 1.000000 -427.233595 178.244528)')
    _text.escaped_text = ''
    _text.children.clear()
    _text.append_line('receive(StopOfferService)', x=4.0000, y=12.0000, direction='ltr', text_anchor='start')
    _text.append_line('/cancelTimer(TTL)', x=4.0000, y=22.0000, direction='ltr', text_anchor='start')
    d.append(_text)

    _path = draw.Path('M -1047.81 -51.26 L -794.85 -51.26', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(0.909259 0.000000 0.000000 0.909259 425.878032 -24.651213)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -794.85 -51.26 L -804.85 -46.26 L -804.85 -56.26 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(0.909259 0.000000 0.000000 0.909259 425.878032 -24.651213)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -713.44 -230.20 L -713.44 -210.20 L -683.44 -210.20 L -683.44 -230.20', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 216.588402 468.944429)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -683.44 -230.20 L -678.44 -220.20 L -688.44 -220.20 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(1.000000 0.000000 0.000000 1.000000 216.588402 468.944429)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -675.35 -251.76 L -535.35 -251.76', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 238.499098 460.504528)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -535.35 -251.76 L -545.35 -246.76 L -545.35 -256.76 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(1.000000 0.000000 0.000000 1.000000 238.499098 460.504528)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -807.01 -149.71 L -1227.01 -149.71 L -1227.01 -99.71', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 220.156099 -41.551200)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1227.01 -99.71 L -1232.01 -109.71 L -1222.01 -109.71 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(1.000000 0.000000 0.000000 1.000000 220.156099 -41.551200)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M 182.43 140.25 L -187.57 140.25 L -187.57 40.25', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -719.282906 78.492365)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -187.57 40.25 L -182.57 50.25 L -192.57 50.25 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(1.000000 0.000000 0.000000 1.000000 -719.282906 78.492365)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M 592.43 110.25 L 592.43 170.25 L -187.57 170.25 L -187.57 50.25', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -849.282906 128.492365)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -187.57 50.25 L -182.57 60.25 L -192.57 60.25 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(1.000000 0.000000 0.000000 1.000000 -849.282906 128.492365)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M 177.01 85.19 L 87.01 85.19 L 87.01 55.19 L 87.01 55.19 L 107.01 55.19', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -713.865375 123.546807)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M 107.01 55.19 L 97.01 60.19 L 97.01 50.19 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(1.000000 0.000000 0.000000 1.000000 -713.865375 123.546807)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -947.50 -222.63 L -947.50 -112.63 L -547.50 -112.63', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 10.652763 341.369214)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -547.50 -112.63 L -557.50 -107.63 L -557.50 -117.63 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(1.000000 0.000000 0.000000 1.000000 10.652763 341.369214)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -1340.15 -106.72 L -1530.15 -106.72 L -1530.15 -56.72', stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='bevel', stroke_miterlimit=4, fill_rule='evenodd', fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 793.303191 -84.544741)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1530.15 -56.72 L -1535.15 -66.72 L -1525.15 -66.72 Z', fill='#000000', fill_opacity=1, stroke='#000000', stroke_opacity=1, stroke_width=2.00, data_pen_units='svg', data_qt_pen_style=1, stroke_linecap='square', stroke_linejoin='miter', stroke_miterlimit=4, fill_rule='evenodd', transform='matrix(1.000000 0.000000 0.000000 1.000000 793.303191 -84.544741)')
    d.append(_arrow_head)
    d.append(_path)

    return d

if __name__ == '__main__':
    d = build_drawing()
    # Creates an SVG file next to the script:
    d.save_svg('feat_req_someipsd_630.svg')
