# Auto-generated from PySide6 Canvas to drawsvg
import drawsvg as draw

def build_drawing():
    d = draw.Drawing(553, 1243, origin=(-373, -538), viewBox='-373 -538 553 1243')
    d.append(draw.Rectangle(-373, -538, 553, 1243, fill='white', stroke='none'))

    _diamond = draw.Lines(-136.85, -531.26, -76.85, -491.26, -136.85, -451.26, -196.85, -491.26, close=True, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='diamond_label_1')
    d.append(_diamond)
    _diamond_label = draw.Text('Received\nMessage Type =\nRequest?', 8.00, -138.65, -492.92, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='diamond_label_1', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='diamond')
    d.append(_diamond_label)

    _rect = draw.Rectangle(-46.85, -451.26, 220.00, 40.00, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_2', rx=21.00, ry=21.00)
    d.append(_rect)
    _rect_label = draw.Text('Send message (Message Type: Response)', 8.00, 63.15, -431.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='rect_label_2', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _path = draw.Path('M -136.85 -451.26 L -136.85 -431.26 L -46.85 -431.26', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -46.85 -431.26 L -55.51 -426.26 L -55.51 -436.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _text = draw.Text('yes', 8.00, -122.85, -447.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _text = draw.Text('no', 8.00, -72.85, -507.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _rect = draw.Rectangle(-366.85, -391.26, 140.00, 60.00, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_3', rx=21.00, ry=21.00)
    d.append(_rect)
    _rect_label = draw.Text('Receive SOME/IP\nMessage and check\ndepending on socket\nreceived on', 8.00, -296.85, -361.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='rect_label_3', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _diamond = draw.Lines(-296.85, -311.26, -236.85, -271.26, -296.85, -231.26, -356.85, -271.26, close=True, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='diamond_label_4')
    d.append(_diamond)
    _diamond_label = draw.Text('Length field < 8\nor received msg does\nnot fit length', 8.00, -298.65, -272.92, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='diamond_label_4', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='diamond')
    d.append(_diamond_label)

    _rect = draw.Rectangle(-196.85, -291.26, 140.00, 40.00, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_5', rx=21.00, ry=21.00)
    d.append(_rect)
    _rect_label = draw.Text('Ignore SOME/IP Message', 8.00, -126.85, -271.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='rect_label_5', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _diamond = draw.Lines(-296.85, -211.26, -236.85, -171.26, -296.85, -131.26, -356.85, -171.26, close=True, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='diamond_label_6')
    d.append(_diamond)
    _diamond_label = draw.Text('Protocol Version\nsupported?', 8.00, -298.65, -172.92, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='diamond_label_6', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='diamond')
    d.append(_diamond_label)

    _rect = draw.Rectangle(-196.85, -191.26, 140.00, 40.00, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_7', rx=21.00, ry=21.00)
    d.append(_rect)
    _rect_label = draw.Text('Ignore SOME/IP Message', 8.00, -126.85, -171.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='rect_label_7', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _diamond = draw.Lines(-296.85, -111.26, -236.85, -81.26, -296.85, -51.26, -356.85, -81.26, close=True, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='diamond_label_8')
    d.append(_diamond)
    _diamond_label = draw.Text('Service ID\nok?', 8.00, -298.64, -82.83, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='diamond_label_8', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='diamond')
    d.append(_diamond_label)

    _rect = draw.Rectangle(-176.85, -101.26, 180.00, 50.00, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_9', rx=20.00, ry=20.00)
    d.append(_rect)
    _rect_label = draw.Text('Optional Answer_behavior (see above)\nProtocol Version = as received\nReturn Code = E_UNKNOWN_SERVICE', 8.00, -86.85, -76.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='rect_label_9', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _rect = draw.Rectangle(-196.85, -11.26, 200.00, 50.00, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_10', rx=21.25, ry=21.25)
    d.append(_rect)
    _rect_label = draw.Text('Answer_behavior (see above)\nProtocol Version = as received\nReturn Code = E_WRONG_INTERFACE_VERSION', 8.00, -96.85, 13.74, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='rect_label_10', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _diamond = draw.Lines(-296.85, -31.26, -236.85, 8.74, -296.85, 48.74, -356.85, 8.74, close=True, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='diamond_label_11')
    d.append(_diamond)
    _diamond_label = draw.Text('Interface\nVersion ok?', 8.00, -298.65, 7.08, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='diamond_label_11', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='diamond')
    d.append(_diamond_label)

    _rect = draw.Rectangle(-196.85, 88.74, 190.00, 50.00, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_12', rx=21.25, ry=21.25)
    d.append(_rect)
    _rect_label = draw.Text('Optional Answer_behavior (see above)\nProtocol Version = as received\nReturn Code = E_UNKNOWN_METHOD', 8.00, -101.85, 113.74, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='rect_label_12', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _diamond = draw.Lines(-296.85, 68.74, -236.85, 108.74, -296.85, 148.74, -356.85, 108.74, close=True, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='diamond_label_13')
    d.append(_diamond)
    _diamond_label = draw.Text('Method ID ok?', 8.00, -298.65, 107.08, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='diamond_label_13', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='diamond')
    d.append(_diamond_label)

    _diamond = draw.Lines(-296.85, 168.74, -236.85, 208.74, -296.85, 248.74, -356.85, 208.74, close=True, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='diamond_label_14')
    d.append(_diamond)
    _diamond_label = draw.Text('Message Type\nsupported?', 8.00, -298.65, 207.08, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='diamond_label_14', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='diamond')
    d.append(_diamond_label)

    _rect = draw.Rectangle(-196.85, 188.74, 140.00, 40.00, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_15', rx=21.00, ry=21.00)
    d.append(_rect)
    _rect_label = draw.Text('Ignore SOME/IP Message', 8.00, -126.85, 208.74, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='rect_label_15', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _diamond = draw.Lines(-296.85, 268.74, -236.85, 308.74, -296.85, 348.74, -356.85, 308.74, close=True, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='diamond_label_16')
    d.append(_diamond)
    _diamond_label = draw.Text('Message Type\nas configured?', 8.00, -298.65, 307.08, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='diamond_label_16', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='diamond')
    d.append(_diamond_label)

    _rect = draw.Rectangle(-196.85, 288.74, 190.00, 50.00, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_17', rx=21.25, ry=21.25)
    d.append(_rect)
    _rect_label = draw.Text('Answer_behavior (see above)\nProtocol Version = as received\nReturn Code = E_WRONG_MESSAGE_TYPE', 8.00, -101.85, 313.74, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='rect_label_17', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _diamond = draw.Lines(-296.85, 368.74, -236.85, 408.74, -296.85, 448.74, -356.85, 408.74, close=True, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='diamond_label_18')
    d.append(_diamond)
    _diamond_label = draw.Text('Message Type =\nResponse or Error?', 8.00, -298.65, 407.08, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='diamond_label_18', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='diamond')
    d.append(_diamond_label)

    _diamond = draw.Lines(-146.85, 368.74, -86.85, 408.74, -146.85, 448.74, -206.85, 408.74, close=True, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='diamond_label_19')
    d.append(_diamond)
    _diamond_label = draw.Text('Client ID\n& Session ID\nknown?', 8.00, -148.65, 407.08, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='diamond_label_19', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='diamond')
    d.append(_diamond_label)

    _rect = draw.Rectangle(-46.85, 388.74, 140.00, 40.00, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_20', rx=21.00, ry=21.00)
    d.append(_rect)
    _rect_label = draw.Text('Ignore SOME/IP Message', 8.00, 23.15, 408.74, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='rect_label_20', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _diamond = draw.Lines(-146.85, 468.74, -86.85, 508.74, -146.85, 548.74, -206.85, 508.74, close=True, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='diamond_label_21')
    d.append(_diamond)
    _diamond_label = draw.Text('Return Code\n= 0 ?', 8.00, -148.65, 507.08, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='diamond_label_21', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='diamond')
    d.append(_diamond_label)

    _rect = draw.Rectangle(-46.85, 488.74, 140.00, 40.00, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_22', rx=21.00, ry=21.00)
    d.append(_rect)
    _rect_label = draw.Text('SOME/IP Service-specific\nError Processing', 8.00, 23.15, 508.74, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='rect_label_22', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _diamond = draw.Lines(-296.85, 558.74, -236.85, 598.74, -296.85, 638.74, -356.85, 598.74, close=True, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='diamond_label_23')
    d.append(_diamond)
    _diamond_label = draw.Text('Payload parseable?', 8.00, -298.65, 597.08, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='diamond_label_23', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='diamond')
    d.append(_diamond_label)

    _rect = draw.Rectangle(-196.85, 578.74, 190.00, 50.00, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_24', rx=21.25, ry=21.25)
    d.append(_rect)
    _rect_label = draw.Text('Answer_behavior (see above)\nProtocol Version = as received\nReturn Code = E_MALFORMED_MESSAGE', 8.00, -101.85, 603.74, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='rect_label_24', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _rect = draw.Rectangle(-366.85, 658.74, 140.00, 40.00, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_25', rx=21.00, ry=21.00)
    d.append(_rect)
    _rect_label = draw.Text('SOME/IP Message\nProcessing', 8.00, -296.85, 678.74, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='rect_label_25', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _path = draw.Path('M -236.85 -271.26 L -196.85 -271.26', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -196.85 -271.26 L -205.51 -266.26 L -205.51 -276.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _text = draw.Text('yes', 8.00, -232.85, -287.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _path = draw.Path('M -236.85 -171.26 L -196.85 -171.26', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -196.85 -171.26 L -205.51 -166.26 L -205.51 -176.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _text = draw.Text('no', 8.00, -232.85, -187.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _text = draw.Text('no', 8.00, -232.85, -97.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _path = draw.Path('M -236.85 8.74 L -196.85 8.74', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -196.85 8.74 L -205.51 13.74 L -205.51 3.74 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _text = draw.Text('no', 8.00, -232.85, 12.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _text = draw.Text('no', 8.00, -232.85, 92.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _path = draw.Path('M -236.85 108.74 L -196.85 108.74', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -196.85 108.74 L -205.51 113.74 L -205.51 103.74 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _path = draw.Path('M -236.85 208.74 L -216.85 208.74 L -196.85 208.74', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -196.85 208.74 L -205.51 213.74 L -205.51 203.74 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _path = draw.Path('M -236.85 308.74 L -196.85 308.74', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -196.85 308.74 L -205.51 313.74 L -205.51 303.74 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _text = draw.Text('no', 8.00, -232.85, 292.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _text = draw.Text('yes', 8.00, -222.85, 392.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _path = draw.Path('M -236.85 408.74 L -206.85 408.74', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -206.85 408.74 L -215.51 413.74 L -215.51 403.74 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _path = draw.Path('M -86.85 408.74 L -46.85 408.74', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -46.85 408.74 L -55.51 413.74 L -55.51 403.74 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _text = draw.Text('no', 8.00, -72.85, 392.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _text = draw.Text('no', 8.00, -72.85, 492.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _path = draw.Path('M -86.85 508.74 L -46.85 508.74', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -46.85 508.74 L -55.51 513.74 L -55.51 503.74 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _text = draw.Text('no', 8.00, -232.85, 582.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _path = draw.Path('M -236.85 598.74 L -196.85 598.74', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -196.85 598.74 L -205.51 603.74 L -205.51 593.74 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _path = draw.Path('M -296.85 -331.26 L -296.85 -311.26', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -296.85 -311.26 L -301.85 -319.92 L -291.85 -319.92 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _path = draw.Path('M -296.85 -231.26 L -296.85 -211.26', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -296.85 -211.26 L -301.85 -219.92 L -291.85 -219.92 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _path = draw.Path('M -296.85 -131.26 L -296.85 -111.26', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -296.85 -111.26 L -301.85 -119.92 L -291.85 -119.92 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _path = draw.Path('M -236.85 -81.26 L -176.85 -81.26', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -176.85 -81.26 L -185.51 -76.26 L -185.51 -86.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _text = draw.Text('no', 8.00, -232.85, 192.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _path = draw.Path('M -296.85 -51.26 L -296.85 -31.26', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -296.85 -31.26 L -301.85 -39.92 L -291.85 -39.92 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _path = draw.Path('M -296.85 48.74 L -296.85 68.74', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -296.85 68.74 L -301.85 60.08 L -291.85 60.08 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _path = draw.Path('M -296.85 148.74 L -296.85 168.74', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -296.85 168.74 L -301.85 160.08 L -291.85 160.08 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _path = draw.Path('M -296.85 248.74 L -296.85 268.74', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -296.85 268.74 L -301.85 260.08 L -291.85 260.08 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _path = draw.Path('M -296.85 348.74 L -296.85 358.74 L -296.85 368.74', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -296.85 368.74 L -301.85 360.08 L -291.85 360.08 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _path = draw.Path('M -146.85 448.74 L -146.85 468.74', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -146.85 468.74 L -151.85 460.08 L -141.85 460.08 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _path = draw.Path('M -296.85 448.74 L -296.85 558.74', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -296.85 558.74 L -301.85 550.08 L -291.85 550.08 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _path = draw.Path('M -206.85 508.74 L -296.85 508.74 L -296.85 558.74', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -296.85 558.74 L -301.85 550.08 L -291.85 550.08 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _path = draw.Path('M -296.85 638.74 L -296.85 658.74', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -296.85 658.74 L -301.85 650.08 L -291.85 650.08 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _text = draw.Text('no', 8.00, -282.85, -227.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _text = draw.Text('yes', 8.00, -282.85, -127.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _text = draw.Text('yes', 8.00, -282.85, -47.26, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _text = draw.Text('yes', 8.00, -282.85, 52.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _text = draw.Text('yes', 8.00, -282.85, 152.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _text = draw.Text('yes', 8.00, -282.85, 252.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _text = draw.Text('yes', 8.00, -282.85, 352.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _text = draw.Text('no', 8.00, -292.85, 452.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _text = draw.Text('yes', 8.00, -132.85, 452.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _text = draw.Text('yes', 8.00, -262.85, 492.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _text = draw.Text('yes', 8.00, -282.85, 632.74, fill='#000000', font_family='Arial', text_anchor='start', dominant_baseline='text-before-edge', alignment_baseline='text-before-edge', data_doc_margin=4.0000, data_font_px=8.0000, data_scale=1.000000)
    d.append(_text)

    _rect = draw.Rectangle(-356.85, -511.26, 110.00, 40.00, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_26', rx=20.00, ry=20.00)
    d.append(_rect)
    _rect_label = draw.Text('Answer_behavior', 8.00, -301.85, -491.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='rect_label_26', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    _path = draw.Path('M -76.85 -491.26 L -46.85 -491.26', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -46.85 -491.26 L -55.51 -486.26 L -55.51 -496.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _path = draw.Path('M -246.85 -491.26 L -196.85 -491.26', stroke='#000000', stroke_width=2.00, fill='none')
    d.append(_path)
    # Arrowheads: start=false, end=true
    _arrow_head = draw.Path('M -196.85 -491.26 L -205.51 -486.26 L -205.51 -496.26 Z', fill='#000000', stroke='#000000', stroke_width=2.00)
    d.append(_arrow_head)

    _rect = draw.Rectangle(-46.85, -511.26, 140.00, 40.00, fill='#ffffff', fill_opacity=1.00, stroke='#000000', stroke_width=2.00, data_label_id='rect_label_27', rx=21.00, ry=21.00)
    d.append(_rect)
    _rect_label = draw.Text('Ignore SOME/IP Message', 8.00, 23.15, -491.26, fill='#000000', font_family='Arial', text_anchor='middle', dominant_baseline='middle', data_shape_label='true', data_label_id='rect_label_27', data_label_h='center', data_label_v='middle', data_font_px=8.0000, data_label_kind='rect', data_rect_label='true')
    d.append(_rect_label)

    return d

if __name__ == '__main__':
    d = build_drawing()
    # Creates an SVG file next to the script:
    d.save_svg('feat_req_someip_718.svg')