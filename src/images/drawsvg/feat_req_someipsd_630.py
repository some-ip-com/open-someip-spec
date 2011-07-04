# Auto-generated from PySide6 Canvas to drawsvg
import drawsvg as draw

def build_drawing():
    d = draw.Drawing(772, 713, origin=(-1163, -548), viewBox='-1163 -548 772 713')
    d.append(draw.Rectangle(-1163, -548, 772, 713, fill='white', stroke='none'))

    _rect = draw.Rectangle(-1156.85, -541.26, 590.00, 700.00, fill='#f9c499', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_1', rx=9.78, ry=9.78)
    d.append(_rect)
    # Multiline label for rect_label_1
    _rect_label = draw.Text("SD Client State Machine (Services)", 12.00, -861.85, -520.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.333333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_1', data_label_h='center', data_label_v='top', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _rect = draw.Rectangle(-1136.85, -111.26, 480.00, 260.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_2', rx=15.18, ry=15.18)
    d.append(_rect)
    # Multiline label for rect_label_2
    _rect_label = draw.Text("Searching for Service", 12.00, -896.85, -90.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.333333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_2', data_label_h='center', data_label_v='top', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _rect = draw.Rectangle(-1046.85, -81.26, 370.00, 80.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_3', rx=9.42, ry=9.42)
    d.append(_rect)
    # Multiline label for rect_label_3
    _rect_label = draw.Text("Initial Wait Phase", 12.00, -861.85, -60.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.333333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_3', data_label_h='center', data_label_v='top', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _text = draw.Text(["/setTimerInRange(INITIAL_DELAY_MIN,", "INITIAL_DELAY_MAX)"], 9.00, -992.85, -47.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=190.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _rect = draw.Rectangle(-646.85, 8.74, 70.00, 50.00, fill='#d9d9d9', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_4')
    d.append(_rect)
    # Multiline label for rect_label_4
    _rect_label = draw.Text(["Request/Release", "omitted in this", "diagram!"], 7.00, -611.85, 26.74, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.285714, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_4', data_label_h='center', data_label_v='middle', data_font_px=7.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _rect = draw.Rectangle(-1116.85, 18.74, 440.00, 110.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_5', rx=9.71, ry=9.71)
    d.append(_rect)
    # Multiline label for rect_label_5
    _rect_label = draw.Text("Repetition Phase", 12.00, -896.85, 39.74, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.333333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_5', data_label_h='center', data_label_v='top', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _text = draw.Text(["[run<REPETITIONS_MAX]", "/sendMessage(FindService)", "run++", "setTimer((2^run)*REPETITIONS_BASE_DELAY)"], 9.00, -942.85, 82.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=300.0000, data_box_h=60.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(" ", 9.00, -582.85, -17.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=190.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _path = draw.Path('M -1056.85 68.74 L -796.85 68.74', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -796.85 68.74 L -806.85 73.74 L -806.85 63.74 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["Timer Expired", "/sendMessage(FindService)"], 9.00, -802.85, -27.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=140.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["[REPETITIONS_MAX>0]", "/run=0", "setTimer((2^run)*REPETITIONS_BASE_DELAY)"], 9.00, -1052.85, 32.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=220.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("Initial", 9.00, -1089.49, 40.89, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=40.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("Initial", 9.00, -1032.14, -75.22, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=40.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("Initial", 9.00, -1112.85, -87.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=40.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["receiveMessage(ServiceOffer)", "/resetTimer(TTL)"], 9.00, -712.85, -197.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=150.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["Timer expired ", "(TTL)"], 9.00, -712.85, -147.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=80.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["[ServiceRequested and", "ifstatus==up_and_configured]"], 9.00, -1072.85, -167.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=140.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["receiveMessage(ServiceOffer)", "/setTimer(TTL)"], 9.00, -882.85, -147.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=160.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["if-status-changed()", "[ifstatus==up_and_configured]"], 9.00, -922.85, -207.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=160.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["[ServiceRequested and", "ifstatus!=up_and_configured]"], 9.00, -1072.85, -227.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=140.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("Initial", 9.00, -1122.85, -247.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=40.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["[ServiceNot", "Requested]"], 9.00, -1132.85, -287.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=70.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["InternalServiceRequest", "[ifstatus!=up_and_configured]"], 9.00, -1042.85, -297.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=160.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["InternalServiceRequest", "[ifstatus==up_and_configured]"], 9.00, -822.85, -297.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=160.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _rect = draw.Rectangle(-1136.85, -501.26, 530.00, 190.00, fill='#f9c499', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_6', rx=13.96, ry=13.96)
    d.append(_rect)
    # Multiline label for rect_label_6
    _rect_label = draw.Text("Not Requested", 12.00, -871.85, -480.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.333333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_6', data_label_h='center', data_label_v='top', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _text = draw.Text(["receiveMessage(ServiceOffer)", "/resetTimer(TTL)"], 9.00, -882.85, -337.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=160.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("Initial", 9.00, -1072.85, -487.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=50.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _path = draw.Path('M -766.85 -401.26 L -1036.85 -401.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1036.85 -401.26 L -1026.85 -406.26 L -1026.85 -396.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -1036.85 -431.26 L -766.85 -431.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -766.85 -431.26 L -776.85 -426.26 L -776.85 -436.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["if-status-changed() [ifstatus!", "=up_and_configured]"], 9.00, -972.85, -427.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=190.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("Timer expired (TTL)", 9.00, -952.85, -397.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=100.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("receiveMessage(StopServiceOffer)", 9.00, -972.85, -377.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=170.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["messageReceived(ServiceOffer)", "/setTimer(TTL)"], 9.00, -972.85, -457.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=160.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _rect = draw.Rectangle(-766.85, -261.26, 160.00, 40.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_7', rx=13.57, ry=13.57)
    d.append(_rect)
    # Multiline label for rect_label_7
    _rect_label = draw.Text("Service Ready", 12.00, -686.85, -236.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.333333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_7', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _rect = draw.Rectangle(-766.85, -441.26, 90.00, 100.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_8', rx=4.05, ry=4.05)
    d.append(_rect)
    # Multiline label for rect_label_8
    _rect_label = draw.Text("Service Seen", 12.00, -721.85, -386.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.333333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_8', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _path = draw.Path('M -1086.85 -471.26 L -1086.85 -451.26 L -1086.85 -441.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1086.85 -441.26 L -1091.85 -451.26 L -1081.85 -451.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -1076.85 -251.26 L -1076.85 -311.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1076.85 -311.26 L -1071.85 -301.26 L -1081.85 -301.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -1086.85 -61.26 L -1046.85 -61.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1046.85 -61.26 L -1056.85 -56.26 L -1056.85 -66.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -676.85 -221.26 L -676.85 -201.26 L -656.85 -201.26 L -656.85 -221.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -656.85 -221.26 L -651.85 -211.26 L -661.85 -211.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -766.85 -381.26 L -1036.85 -381.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1036.85 -381.26 L -1026.85 -386.26 L -1026.85 -376.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -926.85 -221.26 L -926.85 -111.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -926.85 -111.26 L -931.85 -121.26 L -921.85 -121.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _circ = draw.Circle(-1006.85, -51.26, 10.00, fill='#000000', fill_opacity=1.00, stroke='#000000', stroke_width=2.00)
    d.append(_circ)

    _circ = draw.Circle(-1086.85, -481.26, 10.00, fill='#000000', fill_opacity=1.00, stroke='#000000', stroke_width=2.00)
    d.append(_circ)

    _path = draw.Path('M -746.85 -341.26 L -746.85 -321.26 L -726.85 -321.26 L -726.85 -341.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -726.85 -341.26 L -721.85 -331.26 L -731.85 -331.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _circ = draw.Circle(-1096.85, -61.26, 10.00, fill='#000000', fill_opacity=1.00, stroke='#000000', stroke_width=2.00)
    d.append(_circ)

    _rect = draw.Rectangle(-966.85, -261.26, 170.00, 40.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_9', rx=12.77, ry=12.77)
    d.append(_rect)
    # Multiline label for rect_label_9
    _rect_label = draw.Text("Requested_but_not_Ready", 12.00, -881.85, -236.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.333333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_9', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _path = draw.Path('M -776.85 88.74 L -776.85 108.74 L -756.85 108.74 L -756.85 88.74', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -756.85 88.74 L -751.85 98.74 L -761.85 98.74 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _circ = draw.Circle(-1066.85, 68.74, 10.00, fill='#000000', fill_opacity=1.00, stroke='#000000', stroke_width=2.00)
    d.append(_circ)

    _path = draw.Path('M -1006.85 -51.26 L -816.85 -51.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -816.85 -51.26 L -826.85 -46.26 L -826.85 -56.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _circ = draw.Circle(-1076.85, -241.26, 10.00, fill='#000000', fill_opacity=1.00, stroke='#000000', stroke_width=2.00)
    d.append(_circ)

    _path = draw.Path('M -696.85 -341.26 L -696.85 -261.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -696.85 -261.26 L -701.85 -271.26 L -691.85 -271.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -805.69 -35.40 L -806.85 18.74', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -806.85 18.74 L -811.63 8.64 L -801.64 8.85 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _rect = draw.Rectangle(-1126.85, -441.26, 90.00, 100.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_10', rx=4.05, ry=4.05)
    d.append(_rect)
    # Multiline label for rect_label_10
    _rect_label = draw.Text(["Service Not", "     Seen"], 12.00, -1081.85, -394.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.333333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_10', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _path = draw.Path('M -906.85 -311.26 L -906.85 -291.26 L -906.85 -261.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -906.85 -261.26 L -911.85 -271.26 L -901.85 -271.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _rect = draw.Rectangle(-813.93, -64.80, 90.00, 30.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_11', rx=10.18, ry=10.18)
    d.append(_rect)
    # Multiline label for rect_label_11
    _rect_label = draw.Text(" Timer Set", 12.00, -768.93, -44.80, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.333333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_11', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _path = draw.Path('M -726.85 -221.26 L -726.85 -111.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -726.85 -111.26 L -731.85 -121.26 L -721.85 -121.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -766.85 -361.26 L -1036.85 -361.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1036.85 -361.26 L -1026.85 -366.26 L -1026.85 -356.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _rect = draw.Rectangle(-796.85, 48.74, 100.00, 40.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_12', rx=13.57, ry=13.57)
    d.append(_rect)
    # Multiline label for rect_label_12
    _rect_label = draw.Text(" Timer Set", 12.00, -746.85, 73.74, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.333333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_12', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _path = draw.Path('M -1066.85 -241.26 L -966.85 -241.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -966.85 -241.26 L -976.85 -236.26 L -976.85 -246.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -746.85 -111.26 L -746.85 -161.26 L -746.85 -221.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -746.85 -221.26 L -741.85 -211.26 L -751.85 -211.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -1076.85 -231.26 L -1076.85 -111.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1076.85 -111.26 L -1081.85 -121.26 L -1071.85 -121.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    return d

if __name__ == '__main__':
    d = build_drawing()
    # Creates an SVG file next to the script:
    d.save_svg('feat_req_someipsd_630.svg')