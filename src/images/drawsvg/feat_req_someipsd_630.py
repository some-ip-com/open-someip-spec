# Auto-generated from PySide6 Canvas to drawsvg
import drawsvg as draw

def build_drawing():
    d = draw.Drawing(703, 713, origin=(-1162, -518), viewBox='-1162 -518 703 713')
    d.append(draw.Rectangle(-1162, -518, 703, 713, fill='white', stroke='none'))

    _rect = draw.Rectangle(0.00, 0.00, 690.00, 700.00, fill='#f9c499', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_1', rx=9.37, ry=9.37, transform='matrix(1.000000 0.000000 0.000000 1.000000 -1155.850394 -511.260000)')
    d.append(_rect)
    # Multiline label for rect_label_1
    _rect_label = draw.Text("SD Client State Machine (Services)", 12.00, 337.00, 11.00, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_1', data_label_h='center', data_label_v='top', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1147.850394 -503.260000)')
    d.append(_rect_label)

    _rect = draw.Rectangle(0.00, 0.00, 480.00, 260.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_2', rx=15.18, ry=15.18, transform='matrix(1.000000 0.000000 0.000000 1.000000 -1136.850000 -111.260000)')
    d.append(_rect)
    # Multiline label for rect_label_2
    _rect_label = draw.Text("Searching for Service", 12.00, 232.00, 11.00, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_2', data_label_h='center', data_label_v='top', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1128.850000 -103.260000)')
    d.append(_rect_label)

    _rect = draw.Rectangle(0.00, 0.00, 370.00, 80.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_3', rx=9.42, ry=9.42, transform='matrix(1.000000 0.000000 0.000000 1.000000 -1046.850000 -81.260000)')
    d.append(_rect)
    # Multiline label for rect_label_3
    _rect_label = draw.Text("Initial Wait Phase", 12.00, 177.00, 11.00, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_3', data_label_h='center', data_label_v='top', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1038.850000 -73.260000)')
    d.append(_rect_label)

    _text = draw.Text(["/setTimerInRange(INITIAL_DELAY_MIN,", "INITIAL_DELAY_MAX)"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="/setTimerInRange(INITIAL_DELAY_MIN,\nINITIAL_DELAY_MAX)", data_box_w=190.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -996.850000 -51.260000)')
    d.append(_text)

    _rect = draw.Rectangle(0.00, 0.00, 440.00, 110.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_4', rx=9.71, ry=9.71, transform='matrix(1.000000 0.000000 0.000000 1.000000 -1116.850000 18.740000)')
    d.append(_rect)
    # Multiline label for rect_label_4
    _rect_label = draw.Text("Repetition Phase", 12.00, 212.00, 11.00, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_4', data_label_h='center', data_label_v='top', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1108.850000 26.740000)')
    d.append(_rect_label)

    _text = draw.Text(["[run<REPETITIONS_MAX]", "/send(FindService)", "run++", "setTimer((2^run)*REPETITIONS_BASE_DELAY)"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="[run<REPETITIONS_MAX]\n/send(FindService)\nrun++\nsetTimer((2^run)*REPETITIONS_BASE_DELAY)", data_box_w=300.0000, data_box_h=60.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -946.850000 78.740000)')
    d.append(_text)

    _path = draw.Path('M -1056.85 68.74 L -796.85 68.74', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -796.85 68.74 L -806.85 73.74 L -806.85 63.74 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["Timer Expired", "/send(FindService)"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="Timer Expired\n/send(FindService)", data_box_w=140.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -806.850000 -31.260000)')
    d.append(_text)

    _text = draw.Text(["[REPETITIONS_MAX>0]", "/run=0", "setTimer((2^run)*REPETITIONS_BASE_DELAY)"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="[REPETITIONS_MAX>0]\n/run=0\nsetTimer((2^run)*REPETITIONS_BASE_DELAY)", data_box_w=220.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1056.850000 28.740000)')
    d.append(_text)

    _text = draw.Text("Initial", 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="Initial", data_box_w=40.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1093.490000 36.890000)')
    d.append(_text)

    _text = draw.Text("Initial", 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="Initial", data_box_w=40.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1036.140000 -79.220000)')
    d.append(_text)

    _text = draw.Text("Initial", 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="Initial", data_box_w=40.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1116.850000 -91.260000)')
    d.append(_text)

    _text = draw.Text(["receive(OfferService)", "/resetTimer(TTL)"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="receive(OfferService)\n/resetTimer(TTL)", data_box_w=110.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -726.850000 -201.260000)')
    d.append(_text)

    _text = draw.Text(["Timer expired ", "(TTL)"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="Timer expired \n(TTL)", data_box_w=80.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -716.850000 -151.260000)')
    d.append(_text)

    _text = draw.Text(["[ServiceRequested and", "ifstatus==up_and_configured]"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="[ServiceRequested and\nifstatus==up_and_configured]", data_box_w=140.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1076.850000 -151.260000)')
    d.append(_text)

    _text = draw.Text(["receive(OfferService)", "/setTimer(TTL)"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="receive(OfferService)\n/setTimer(TTL)", data_box_w=110.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -856.850000 -191.260000)')
    d.append(_text)

    _text = draw.Text(["if-status-changed()", "[ifstatus==up_and_configured]"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="if-status-changed()\n[ifstatus==up_and_configured]", data_box_w=160.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -896.850000 -151.260000)')
    d.append(_text)

    _text = draw.Text(["[ServiceRequested and", "ifstatus!=up_and_configured]"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="[ServiceRequested and\nifstatus!=up_and_configured]", data_box_w=140.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1076.850000 -231.260000)')
    d.append(_text)

    _text = draw.Text("Initial", 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="Initial", data_box_w=40.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1126.850000 -251.260000)')
    d.append(_text)

    _text = draw.Text(["[ServiceNot", "Requested]"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="[ServiceNot\nRequested]", data_box_w=70.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1136.850000 -291.260000)')
    d.append(_text)

    _text = draw.Text(["InternalServiceRequest", "[ifstatus!=up_and_configured]"], 9.33, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text="InternalServiceRequest\n[ifstatus!=up_and_configured]", data_box_w=160.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1046.850000 -301.260000)')
    d.append(_text)

    _text = draw.Text(["InternalServiceRequest", "[ifstatus==up_and_confi", "gured]"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="InternalServiceRequest\n[ifstatus==up_and_configured]", data_box_w=120.0000, data_box_h=50.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -696.850000 -311.260000)')
    d.append(_text)

    _rect = draw.Rectangle(0.00, 0.00, 480.00, 190.00, fill='#f9c499', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_5', rx=12.64, ry=12.64, transform='matrix(1.000000 0.000000 0.000000 1.000000 -1136.850000 -500.260000)')
    d.append(_rect)
    # Multiline label for rect_label_5
    _rect_label = draw.Text("Not Requested", 12.00, 232.00, 11.00, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_5', data_label_h='center', data_label_v='top', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1128.850000 -492.260000)')
    d.append(_rect_label)

    _text = draw.Text(["receive(OfferService)", "/resetTimer(TTL)"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="receive(OfferService)\n/resetTimer(TTL)", data_box_w=110.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -776.850000 -501.260000)')
    d.append(_text)

    _text = draw.Text("Initial", 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="Initial", data_box_w=50.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1076.850000 -491.260000)')
    d.append(_text)

    _path = draw.Path('M -766.85 -401.26 L -1036.85 -401.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1036.85 -401.26 L -1026.85 -406.26 L -1026.85 -396.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -1036.85 -431.26 L -766.85 -431.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -766.85 -431.26 L -776.85 -426.26 L -776.85 -436.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["if-status-changed() [ifstatus!", "=up_and_configured]"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="if-status-changed() [ifstatus!\n=up_and_configured]", data_box_w=190.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -976.850000 -431.260000)')
    d.append(_text)

    _text = draw.Text("Timer expired (TTL)", 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="Timer expired (TTL)", data_box_w=100.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -956.850000 -401.260000)')
    d.append(_text)

    _text = draw.Text("receive(StopOffeServicer)", 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="receive(StopOffeServicer)", data_box_w=170.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -976.850000 -371.260000)')
    d.append(_text)

    _text = draw.Text(["receive(OfferService)", "/setTimer(TTL)"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="receive(OfferService)\n/setTimer(TTL)", data_box_w=160.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -966.850000 -461.260000)')
    d.append(_text)

    _rect = draw.Rectangle(0.00, 0.00, 100.00, 40.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_6', rx=8.48, ry=8.48, transform='matrix(1.000000 0.000000 0.000000 1.000000 -766.850000 -261.260000)')
    d.append(_rect)
    # Multiline label for rect_label_6
    _rect_label = draw.Text("Service Ready", 12.00, 42.00, 11.00, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_6', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -758.850000 -248.260000)')
    d.append(_rect_label)

    _rect = draw.Rectangle(0.00, 0.00, 90.00, 100.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_7', rx=4.05, ry=4.05, transform='matrix(1.000000 0.000000 0.000000 1.000000 -766.850000 -441.260000)')
    d.append(_rect)
    # Multiline label for rect_label_7
    _rect_label = draw.Text("Service Seen", 12.00, 37.00, 11.00, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_7', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -758.850000 -398.260000)')
    d.append(_rect_label)

    _path = draw.Path('M -1086.85 -471.26 L -1086.85 -451.26 L -1086.85 -441.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1086.85 -441.26 L -1091.85 -451.26 L -1081.85 -451.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -1076.85 -251.26 L -1076.85 -311.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1076.85 -311.26 L -1071.85 -301.26 L -1081.85 -301.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -1086.85 -61.26 L -1046.85 -61.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1046.85 -61.26 L -1056.85 -56.26 L -1056.85 -66.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -716.85 -221.26 L -716.85 -201.26 L -696.85 -201.26 L -696.85 -221.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -696.85 -221.26 L -691.85 -211.26 L -701.85 -211.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -766.85 -381.26 L -1036.85 -381.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1036.85 -381.26 L -1026.85 -386.26 L -1026.85 -376.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -896.85 -221.26 L -896.85 -111.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -896.85 -111.26 L -901.85 -121.26 L -891.85 -121.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _circ = draw.Circle(10.00, 10.00, 10.00, fill='#000000', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -1016.850000 -61.260000)')
    d.append(_circ)

    _circ = draw.Circle(10.00, 10.00, 10.00, fill='#000000', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -1096.850000 -491.260000)')
    d.append(_circ)

    _circ = draw.Circle(10.00, 10.00, 10.00, fill='#000000', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -1106.850000 -71.260000)')
    d.append(_circ)

    _rect = draw.Rectangle(0.00, 0.00, 170.00, 40.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_8', rx=12.77, ry=12.77, transform='matrix(1.000000 0.000000 0.000000 1.000000 -966.850000 -261.260000)')
    d.append(_rect)
    # Multiline label for rect_label_8
    _rect_label = draw.Text("Requested_but_not_Ready", 12.00, 77.00, 11.00, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_8', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -958.850000 -248.260000)')
    d.append(_rect_label)

    _path = draw.Path('M -776.85 88.74 L -776.85 108.74 L -756.85 108.74 L -756.85 88.74', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -756.85 88.74 L -751.85 98.74 L -761.85 98.74 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _circ = draw.Circle(10.00, 10.00, 10.00, fill='#000000', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -1076.850000 58.740000)')
    d.append(_circ)

    _path = draw.Path('M -1006.85 -51.26 L -816.85 -51.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -816.85 -51.26 L -826.85 -46.26 L -826.85 -56.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _circ = draw.Circle(10.00, 10.00, 10.00, fill='#000000', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -1086.850000 -251.260000)')
    d.append(_circ)

    _path = draw.Path('M -696.85 -341.26 L -696.85 -261.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -696.85 -261.26 L -701.85 -271.26 L -691.85 -271.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -805.69 -35.40 L -806.85 18.74', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -806.85 18.74 L -811.63 8.64 L -801.64 8.85 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _rect = draw.Rectangle(0.00, 0.00, 90.00, 100.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_9', rx=4.05, ry=4.05, transform='matrix(1.000000 0.000000 0.000000 1.000000 -1126.850000 -441.260000)')
    d.append(_rect)
    # Multiline label for rect_label_9
    _rect_label = draw.Text(["Service Not", "     Seen"], 12.00, 37.00, 11.00, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_9', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1118.850000 -405.260000)')
    d.append(_rect_label)

    _path = draw.Path('M -906.85 -311.26 L -906.85 -291.26 L -906.85 -261.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -906.85 -261.26 L -911.85 -271.26 L -901.85 -271.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _rect = draw.Rectangle(0.00, 0.00, 90.00, 30.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_10', rx=10.18, ry=10.18, transform='matrix(1.000000 0.000000 0.000000 1.000000 -813.930000 -64.800000)')
    d.append(_rect)
    # Multiline label for rect_label_10
    _rect_label = draw.Text(" Timer Set", 12.00, 37.00, 11.00, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_10', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -805.930000 -56.800000)')
    d.append(_rect_label)

    _path = draw.Path('M -736.85 -221.26 L -736.85 -111.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -736.85 -111.26 L -741.85 -121.26 L -731.85 -121.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -766.85 -351.26 L -1036.85 -351.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1036.85 -351.26 L -1026.85 -356.26 L -1026.85 -346.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _rect = draw.Rectangle(0.00, 0.00, 100.00, 40.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_11', rx=13.57, ry=13.57, transform='matrix(1.000000 0.000000 0.000000 1.000000 -796.850000 48.740000)')
    d.append(_rect)
    # Multiline label for rect_label_11
    _rect_label = draw.Text(" Timer Set", 12.00, 42.00, 11.00, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_11', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -788.850000 61.740000)')
    d.append(_rect_label)

    _path = draw.Path('M -1066.85 -241.26 L -966.85 -241.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -966.85 -241.26 L -976.85 -236.26 L -976.85 -246.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -756.85 -111.26 L -756.85 -161.26 L -756.85 -221.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -756.85 -221.26 L -751.85 -211.26 L -761.85 -211.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -1076.85 -231.26 L -1076.85 -111.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1076.85 -111.26 L -1081.85 -121.26 L -1071.85 -121.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -916.85 -111.26 L -916.85 -161.26 L -916.85 -221.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -916.85 -221.26 L -911.85 -211.26 L -921.85 -211.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["if-status-changed()", "[ifstatus!", "=up_and_configured]", "/cancelTimer(TTL)"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="if-status-changed()\n[ifstatus!\n=up_and_configured]\n/cancelTimer(TTL)", data_box_w=110.0000, data_box_h=50.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -1006.850000 -201.260000)')
    d.append(_text)

    _rect = draw.Rectangle(0.00, 0.00, 100.00, 40.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_12', rx=8.48, ry=8.48, transform='matrix(1.000000 0.000000 0.000000 1.000000 -576.850000 -261.260000)')
    d.append(_rect)
    # Multiline label for rect_label_12
    _rect_label = draw.Text("Stopped", 12.00, 42.00, 11.00, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_12', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_color_override='true', data_label_kind='rect', data_rect_label='true', transform='matrix(1.000000 0.000000 0.000000 1.000000 -568.850000 -248.260000)')
    d.append(_rect_label)

    _path = draw.Path('M -666.85 -251.26 L -576.85 -251.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -576.85 -251.26 L -586.85 -246.26 L -586.85 -256.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -576.14 -238.43 L -666.14 -238.43', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -666.14 -238.43 L -656.14 -243.43 L -656.14 -233.43 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 0.000000 0.000000)')
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["receive(StopOfferService)", "/cancelTimer(TTL)"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="receive(StopOfferService)\n/cancelTimer(TTL)", data_box_w=140.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -666.850000 -281.260000)')
    d.append(_text)

    _text = draw.Text(["receive(OfferService)", "/resetTimer(TTL)"], 9.00, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_raw_text="receive(OfferService)\n/resetTimer(TTL)", data_box_w=110.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -668.270000 -229.840000)')
    d.append(_text)

    _path = draw.Path('M -365.40 -519.26 L -364.93 -548.20 L -404.93 -548.20 L -404.93 -518.20', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -341.919267 76.944037)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -404.93 -518.20 L -409.93 -528.20 L -399.93 -528.20 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -341.919267 76.944037)')
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M 0.00 0.00 L -1.11 -80.00', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -725.935669 -262.316744)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1.11 -80.00 L 4.03 -70.07 L -5.97 -69.93 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -725.935669 -262.316744)')
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text("[ServiceNotRequested]", 9.33, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text="[ServiceNotRequested]", data_box_w=120.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -830.328528 -334.092603)')
    d.append(_text)

    _path = draw.Path('M 62.56 15.00 L 62.56 -5.00 L -59.00 -5.00 L -59.00 15.00', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -799.415124 -276.260157)')
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -59.00 15.00 L -64.00 5.00 L -54.00 5.00 Z', fill='#000000', stroke='#000000', stroke_width=2.00, transform='matrix(1.000000 0.000000 0.000000 1.000000 -799.415124 -276.260157)')
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["if-status-changed()[ifstatus!", "=up_and_configured]"], 9.33, 4.00, 4.00, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.071429, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.3333, data_scale=1.000000, data_raw_text="if-status-changed()[ifstatus!=up_and_configured]", data_box_w=150.0000, data_box_h=30.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr', transform='matrix(1.000000 0.000000 0.000000 1.000000 -886.850000 -311.260000)')
    d.append(_text)

    return d

if __name__ == '__main__':
    d = build_drawing()
    # Creates an SVG file next to the script:
    d.save_svg('feat_req_someipsd_630.svg')
