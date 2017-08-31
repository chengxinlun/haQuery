def iriAnalysis(iriClassList):
    # Time tag
    timeList = [each.tag[0] for each in iriClassList]
    # Mag tag
    magList = [each.tag[1] for each in iriClassList]
    # Alt tag
    altList = [each.tag[2] for each in iriClassList]
    # General statistics for time distribution
    nDawn = 0
    lDusk = []
    for i in range(len(timeList)):
        if timeList[i] == 'dwn':
            nDawn += 1
        elif timeList[i] == 'dsk':
            lDusk.append(i)
    nDusk = len(lDusk)
    # Time distribution description
    if len(timeList) > 8:
        bactive = True
        active = "比较活跃"
    else:
        bactive = False
        active = "活跃度一般"
    text = "本周铱星闪光" + active + '，'
    if nDusk == 0:
        if not bactive:
            text = text + "且全部发生在夜间或者凌晨，不太适合观测。"
        else:
            text = text + "但全部发生在夜间或者凌晨，不太适合观测。"
        return text
    elif nDawn > 0.75 * len(timeList):
        text = text + "大多发生在凌晨。"
    elif nDusk > 0.75 * len(timeList):
        text = text + "大多发生在傍晚。"
    else:
        text = text + "凌晨与傍晚均有分布。"
    # Check if bright enough
    lBright = []
    for i in lDusk:
        if magList[i] == 'brt':
            lBright.append(i)
    nBright = len(lBright)
    # Brightness distribution description
    if nBright == 0:
        text = text + "闪光普遍亮度较暗，不适合观测。"
        return text
    else:
        text = text + "共有" + str(nBright) + "次亮度超过金星，且发生在傍晚。"
    # Check if high enough
    lHigh = []
    for i in lBright:
        if altList[i] == 'hgh':
            lHigh.append(i)
    nHigh = len(lHigh)
    # Altitude distribution description
    if nHigh == 0:
        text = text + "但由于高度均较低，不适合在校园内观测。"
    elif nBright != nHigh:
        text = text + "其中有" + str(nBright - nHigh) + "次由于高度不够，不适合观测。"
    text = text + "\n重点关注："
    for each in lHigh:
        text = text + iriClassList[each].dt.strftime("%m月%d日%H:%M:%S") + "\n"
    return text
