# Auto-generated from PySide6 Canvas to drawsvg
import drawsvg as draw

def build_drawing():
    d = draw.Drawing(633, 463, origin=(-1163, -548), viewBox='-1163 -548 633 463')
    d.append(draw.Rectangle(-1163, -548, 633, 463, fill='white', stroke='none'))

    _rect = draw.Rectangle(-1156.85, -541.26, 620.00, 450.00, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00)
    d.append(_rect)

    _rect = draw.Rectangle(-1136.85, -521.26, 580.00, 420.00, fill='#f9c499', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_1', rx=41.69, ry=41.69)
    d.append(_rect)
    # Multiline label for rect_label_1
    _rect_label = draw.Text("Eventgroup_PubSub (Multicast Eventgroup)", 12.00, -846.85, -502.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_1', data_label_h='center', data_label_v='top', data_font_px=12.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _rect = draw.Rectangle(-1116.85, -401.26, 540.00, 280.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_2', rx=15.88, ry=15.88)
    d.append(_rect)
    # Multiline label for rect_label_2
    _rect_label = draw.Text("Service Up", 12.00, -846.85, -382.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_2', data_label_h='center', data_label_v='top', data_font_px=12.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _path = draw.Path('M -676.85 -191.26 L -696.85 -191.26 L -696.85 -171.26 L -684.30 -170.79 L -676.85 -171.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -676.85 -171.26 L -686.52 -165.64 L -687.14 -175.62 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -676.85 -341.26 L -696.85 -341.26 L -696.85 -321.26 L -676.85 -321.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -676.85 -321.26 L -686.85 -316.26 L -686.85 -326.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["receive(SubscribeEventgroup)", "/SubscriptionCounter++", "send(SubscribeEventgroupAck)"], 9.00, -812.85, -317.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=150.0000, data_box_h=50.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _path = draw.Path('M -676.85 -201.26 L -956.85 -201.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -956.85 -201.26 L -946.85 -206.26 L -946.85 -196.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _text = draw.Text(["receive(StopSubscribeEventgroup) ", "[SubscriptionCounter>1]", "/SubscriptionCounter--"], 9.00, -832.85, -237.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=170.0000, data_box_h=50.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["TTL_expired ", "[SubscriptionCounter>1]", "/SubscriptionCounter--"], 9.00, -802.85, -187.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=120.0000, data_box_h=40.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["receive(StopSubscribeEventgroup) ", "[SubscriptionCounter==1]", "/SubscriptionCounter--", "disableEvents()"], 9.00, -952.85, -267.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=170.0000, data_box_h=60.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["receive(SubscribeEventgroup)", "/enableEvents()", "SubscriptionCounter++", "send(SubscribeEventgroupAck)"], 9.00, -952.85, -357.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=190.0000, data_box_h=60.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text(["TTL_expired ", "[SubscriptionCounter==1]", "/SubscriptionCounter--", "disableEvents()"], 9.00, -942.85, -197.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=130.0000, data_box_h=50.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _path = draw.Path('M -693.45 -402.20 L -694.96 -456.23 L -755.28 -456.23', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -755.28 -456.23 L -745.28 -461.23 L -745.28 -451.23 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _circ = draw.Circle(-1086.85, -341.26, 10.00, fill='#000000', fill_opacity=1.00, stroke='#000000', stroke_width=2.00)
    d.append(_circ)

    _path = draw.Path('M -1037.70 -461.89 L -916.85 -461.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -916.85 -461.26 L -926.88 -456.31 L -926.82 -466.31 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _rect = draw.Rectangle(-676.85, -371.26, 80.00, 230.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_3', rx=9.00, ry=9.00)
    d.append(_rect)
    # Multiline label for rect_label_3
    _rect_label = draw.Text("Subscribed", 12.00, -636.85, -252.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_3', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _rect = draw.Rectangle(-1036.85, -381.26, 80.00, 230.00, fill='#f9c499', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_4', rx=9.00, ry=9.00)
    d.append(_rect)
    # Multiline label for rect_label_4
    _rect_label = draw.Text(["Not", "Subscribed"], 12.00, -996.85, -269.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_4', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _rect = draw.Rectangle(-666.85, -501.26, 100.00, 50.00, fill='#d9d9d9', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_5')
    d.append(_rect)
    # Multiline label for rect_label_5
    _rect_label = draw.Text(["OfferService is implicit", "PublishEventgroup"], 9.00, -658.85, -483.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='alphabetic', line_height=1.111111, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_5', data_label_h='left', data_label_v='middle', data_font_px=9.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _path = draw.Path('M -756.86 -470.03 L -679.13 -470.67 L -676.85 -401.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -676.85 -401.26 L -682.18 -411.09 L -672.18 -411.42 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _circ = draw.Circle(-1036.85, -461.26, 10.00, fill='#000000', fill_opacity=1.00, stroke='#000000', stroke_width=2.00)
    d.append(_circ)

    _rect = draw.Rectangle(-1156.85, -541.26, 340.00, 20.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_6')
    d.append(_rect)
    # Multiline label for rect_label_6
    _rect_label = draw.Text("stm Service Discovery Eventgroup Pub/Sub (Multicast)", 12.00, -986.85, -527.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_6', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _path = draw.Path('M -956.85 -361.26 L -678.82 -359.38', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -678.82 -359.38 L -688.85 -354.45 L -688.79 -364.45 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -676.85 -261.26 L -696.85 -261.26 L -696.85 -241.26 L -676.85 -241.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -676.85 -241.26 L -686.85 -236.26 L -686.85 -246.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -678.82 -271.02 L -816.85 -271.26 L -956.85 -271.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -956.85 -271.26 L -946.85 -276.26 L -946.85 -266.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -1076.85 -341.26 L -1036.85 -341.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1036.85 -341.26 L -1046.85 -336.26 L -1046.85 -346.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _path = draw.Path('M -1036.85 -461.26 L -1036.85 -401.26', stroke='#000000', stroke_width=2.00, fill='none', data_arrow_start=False, data_arrow_end=True, data_arrow_head_length=10.00, data_arrow_head_width=10.00)
    # Arrowheads: start=false, end=true, length=10.00, width=10.00
    _arrow_head = draw.Path('M -1036.85 -401.26 L -1041.85 -411.26 L -1031.85 -411.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)
    d.append(_path)

    _rect = draw.Rectangle(-916.85, -481.26, 160.00, 40.00, fill='none', stroke='#000000', stroke_width=2.00, data_label_id='rect_label_7', rx=7.20, ry=7.20)
    d.append(_rect)
    # Multiline label for rect_label_7
    _rect_label = draw.Text("Service Down", 12.00, -836.85, -457.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='alphabetic', line_height=1.083333, xml__space='preserve', data_shape_label='true', data_label_id='rect_label_7', data_label_h='center', data_label_v='middle', data_font_px=12.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _text = draw.Text("Initial", 9.00, -1082.85, -467.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=40.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("Initial", 9.00, -1099.08, -370.89, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=40.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("[Service==Down]", 9.00, -1022.85, -477.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=100.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("[Service==Up]", 9.00, -1032.85, -437.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=80.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("ServiceDown", 9.00, -762.85, -427.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=80.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    _text = draw.Text("ServiceUp", 9.00, -748.10, -483.31, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', line_height=1.111111, xml__space='preserve', data_doc_margin=4.0000, data_font_px=9.0000, data_scale=1.000000, data_box_w=80.0000, data_box_h=20.0000, data_text_h='left', data_text_v='top', data_text_dir='ltr')
    d.append(_text)

    return d

if __name__ == '__main__':
    d = build_drawing()
    # Creates an SVG file next to the script:
    d.save_svg('canvas.svg')