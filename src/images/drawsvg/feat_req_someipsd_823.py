# Auto-generated from PySide6 Canvas to drawsvg
import drawsvg as draw

def build_drawing():
    d = draw.Drawing(703, 853, origin=(-1183, -558), viewBox='-1183 -558 703 853')
    d.append(draw.Rectangle(-1183, -558, 703, 853, fill='white', stroke='none'))

    _rect = draw.Rectangle(-1176.85, -551.26, 690.00, 840.00, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00)
    d.append(_rect)

    _rect = draw.Rectangle(-1156.85, -531.26, 660.00, 810.00, fill='#f9c499', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_1', rx=25.00, ry=25.00)
    d.append(_rect)
    # Multiline label for rect_label_1
    _rect_label = draw.Text("Eventgroup_PubSub (Unicast-to-Multicast Eventgroup)", 12.00, -826.85, -512.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_1', data_label_h='center', data_label_v='top', data_font_px=12.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _rect = draw.Rectangle(-1136.85, -431.26, 620.00, 640.00, fill='#f9c499', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, rx=17.48, ry=17.48)
    d.append(_rect)

    _path = draw.Path('M -636.85 -201.26 L -656.85 -201.26 L -656.85 -181.26 L -656.85 -181.26 L -636.85 -181.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -636.85 -181.26 L -646.85 -176.26 L -646.85 -186.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["receive(StopSubscribeEventgroup)", "[SubscriptionCounter==1]", "/SubscriptionCounter--", "disableEvents()"], 9.00, -902.85, -307.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=180.0000, data_box_h=60.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _path = draw.Path('M -918.07 -316.76 L -637.56 -315.60', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -637.56 -315.60 L -647.58 -310.64 L -647.54 -320.64 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -916.85 28.74 L -896.85 28.74 L -896.85 28.74 L -896.85 8.74 L -916.85 8.74', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -916.85 8.74 L -906.85 3.74 L -906.85 13.74 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["TTL_expired", "[SubscriptionCounter==1]", "/SubscriptionCounter--", "disableEvents()"], 9.00, -902.85, -237.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=130.0000, data_box_h=60.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["receive(SubscribeEventgroup)", "[UnicastLimit==0]", "/enableMulticastEvents()", "SubscriptionCounter++", "send(SubscribeEventgroupAck)"], 9.00, -922.85, -167.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=170.0000, data_box_h=60.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _path = draw.Path('M -916.85 128.74 L -776.85 128.74 L -636.85 128.74', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -636.85 128.74 L -646.85 133.74 L -646.85 123.74 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -915.35 118.61 L -887.70 118.74 L -887.70 118.74 L -887.70 98.74 L -887.70 98.74 L -917.70 98.74', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -917.70 98.74 L -907.70 93.74 L -907.70 103.74 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["TTL_expired", "[SubscriptionCounter==UnicastLimit+1]", "/switchToUnicastEvents()", "SubscriptionCounter--"], 9.00, -802.85, 132.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=180.0000, data_box_h=60.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["TTL_expired", "[SubscriptionCounter>UnicastLimit+1]", "/SubscriptionCounter--"], 9.00, -882.27, 89.27, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=180.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["receive(StopSubscribeEventgroup)", "[SubscriptionCounter==UnicastLimit+1]", "/switchToUnicastEvents()", "SubscriptionCounter--"], 9.00, -802.85, 33.78, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=180.0000, data_box_h=50.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["receive(StopSubscribeEventgroup)", "[SubscriptionCounter>UnicastLimit+1]", "/SubscriptionCounter--"], 9.00, -891.15, -1.97, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=180.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["receive(SubscribeEventgroup)", "[SubscriptionCounter>=UnicastLimit]", "/SubscriptionCounter++", "send(SubscribeEventgroupAck)", "switchToMulticastEvents()"], 9.00, -792.20, -65.83, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=170.0000, data_box_h=60.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["receive(SubscribeEventgroup)", "/SubscriptionCounter++"], 9.00, -892.85, -87.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=150.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["TTL_expired", "[SubscriptionCounter==1 &&", "UnicastLimit==0]", "/SubscriptionCounter--", "disableMulticastEvents()"], 9.00, -1082.85, -217.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=170.0000, data_box_h=60.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["receive(StopSubscribe", "Eventgroup)", "[SubscriptionCounter==1 &&", "UnicastLimit==0]", "/SubscriptionCounter--", "disableMulticastEvents()"], 9.00, -1072.85, -147.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=140.0000, data_box_h=60.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["TTL_expired", "[SubscriptionCounter>1]", "/SubscriptionCounter--"], 9.00, -742.85, -147.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=120.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["receive(StopSubscribeEventgroup)", "[SubscriptionCounter>1]", "/SubscriptionCounter--"], 9.00, -782.85, -217.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=170.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["receive(SubscribeEventgroup)", "[UnicastLimit>SubscriptionCounter]", "/SubscriptionCounter++", "send(SubscribeEventgroupAck)"], 9.00, -772.85, -397.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=170.0000, data_box_h=50.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["receive(SubscribeEventgroup)", "[UnicastLimit>0]", "/enableEvents()", "SubscriptionCounter++", "send(SubscribeEventgroupAck)"], 9.00, -912.85, -377.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=160.0000, data_box_h=60.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("Initial", 9.00, -1042.85, -407.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=40.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("ServiceDown", 9.00, -796.25, -446.24, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=80.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("ServiceUp", 9.00, -782.85, -487.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=60.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("[Service==Up]", 9.00, -1048.14, -451.61, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=80.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("[Service==Down]", 9.00, -1002.85, -487.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=90.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("Initial", 9.00, -1102.85, -477.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=40.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _rect = draw.Rectangle(-1176.85, -551.26, 380.00, 20.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_2')
    d.append(_rect)
    # Multiline label for rect_label_2
    _rect_label = draw.Text("stm Service Discovery Eventgroup Pub/Sub (Unicast to Multicast)", 12.00, -1168.85, -537.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_2', data_label_h='left', data_label_v='middle', data_font_px=12.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _path = draw.Path('M -731.89 -430.55 L -731.89 -460.55 L -791.89 -460.55', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -791.89 -460.55 L -781.89 -465.55 L -781.89 -455.55 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _circ = draw.Circle(-1056.85, -471.26, 10.00, fill='#000000', fill_opacity=1.00, stroke='#000000', stroke_width=2.00)
    d.append(_circ)

    _path = draw.Path('M -636.85 -171.26 L -656.85 -171.26 L -656.85 -151.26 L -656.85 -151.26 L -636.85 -151.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -636.85 -151.26 L -646.85 -146.26 L -646.85 -156.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -932.42 -220.89 L -932.51 -188.43 L -932.00 -70.52', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -932.00 -70.52 L -937.04 -80.50 L -927.04 -80.54 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -914.30 76.32 L -774.30 76.32 L -634.30 76.32', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -634.30 76.32 L -644.30 81.32 L -644.30 71.32 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _rect = draw.Rectangle(-873.45, -489.56, 80.00, 40.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_3', rx=9.60, ry=9.60)
    d.append(_rect)
    # Multiline label for rect_label_3
    _rect_label = draw.Text(["Service", "Down"], 12.00, -833.45, -472.56, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_3', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _path = draw.Path('M -636.85 -351.26 L -666.85 -351.26 L -666.85 -331.26 L -636.85 -331.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -636.85 -331.26 L -646.85 -326.26 L -646.85 -336.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _rect = draw.Rectangle(-1106.85, -71.26, 190.00, 260.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_4', rx=2.33, ry=2.33)
    d.append(_rect)
    # Multiline label for rect_label_4
    _rect_label = draw.Text(["Subscribed ", "(Multicast)"], 12.00, -1011.85, 55.74, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_4', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _rect = draw.Rectangle(-1106.85, -350.55, 190.00, 130.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_5', rx=2.51, ry=2.51)
    d.append(_rect)
    # Multiline label for rect_label_5
    _rect_label = draw.Text("Not Subscribed", 12.00, -1011.85, -281.55, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_5', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _path = draw.Path('M -1056.85 -461.26 L -1056.85 -431.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1056.85 -431.26 L -1061.85 -441.26 L -1051.85 -441.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _rect = draw.Rectangle(-636.85, -371.26, 100.00, 560.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_6', rx=3.60, ry=3.60)
    d.append(_rect)
    # Multiline label for rect_label_6
    _rect_label = draw.Text(["Subscribed", "(Unicast)"], 12.00, -586.85, -94.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_6', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _path = draw.Path('M -635.04 -13.30 L -914.30 -13.22', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -914.30 -13.22 L -904.30 -18.22 L -904.30 -8.22 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _circ = draw.Circle(-996.85, -401.26, 10.00, fill='#000000', fill_opacity=1.00, stroke='#000000', stroke_width=2.00)
    d.append(_circ)

    _path = draw.Path('M -947.29 -73.06 L -947.69 -219.75', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -947.69 -219.75 L -942.66 -209.76 L -952.66 -209.74 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -794.02 -471.26 L -714.02 -471.26 L -714.02 -431.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -714.02 -431.26 L -719.02 -441.26 L -709.02 -441.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -916.85 -41.26 L -896.85 -41.26 L -896.85 -61.26 L -916.85 -61.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -916.85 -61.26 L -906.85 -66.26 L -906.85 -56.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _rect = draw.Rectangle(-1116.85, 218.74, 300.00, 40.00, fill='#d9d9d9', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_7')
    d.append(_rect)
    # Multiline label for rect_label_7
    _rect_label = draw.Text("Receiving SubscribeEventgroup triggers sendInitialEvents", 8.00, -1108.85, 241.24, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='alphabetic', line_height=1.125000, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_7', data_label_h='left', data_label_v='middle', data_font_px=8.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _path = draw.Path('M -635.04 -241.65 L -916.85 -241.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -916.85 -241.26 L -906.86 -246.27 L -906.84 -236.27 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -635.89 -261.19 L -916.85 -261.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -916.85 -261.26 L -906.85 -266.26 L -906.85 -256.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -1056.85 -471.26 L -876.85 -471.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -876.85 -471.26 L -886.85 -466.26 L -886.85 -476.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -1090.87 -73.91 L -1092.12 -218.90', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1092.12 -218.90 L -1087.03 -208.94 L -1097.03 -208.86 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -996.85 -391.26 L -996.85 -351.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -996.85 -351.26 L -1001.85 -361.26 L -991.85 -361.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    return d

if __name__ == '__main__':
    d = build_drawing()
    # Creates an SVG file next to the script:
    d.save_svg('canvas.svg')
