import ui

def permission_calc(sender):
	'@type sender: ui.Button'
	ReadOwner = 0
	ReadGroup = 0
	ReadOther = 0
	WriteOwner = 0
	WriteGroup = 0
	WriteOther = 0
	ExcuteOwner = 0
	ExcuteGroup = 0
	ExcuteOther = 0
	Total_Owner_String = ''
	Total_Group_String = ''
	Total_Other_String = ''
	
	y = sender.superview
	
	# Read
	read_owner = y['Owner-Read1'].value
	if read_owner:
		ReadOwner = 4
	else:
		ReadOwner = 0
	read_group = y['Group-Read1'].value
	if read_group:
		ReadGroup = 4
	else:
		ReadGroup = 0
	read_other = y['Other-Read1'].value
	if read_other:
		ReadOther = 4
	else:
		ReadOther = 0
	
	# Write
	write_owner = y['Owner-Write2'].value
	if write_owner:
		WriteOwner = 2
	else:
		WriteOwner = 0
	write_group = y['Group-Write2'].value
	if write_group:
		WriteGroup = 2
	else:
		WriteGroup = 0
	write_other = y['Other-Write2'].value
	if write_other:
		WriteOther = 2
	else:
		WriteOther = 0
	
	# Execute
	excute_owner = y['Owner-Excute3'].value
	if excute_owner:
		ExcuteOwner = 1
	else:
		ExcuteOwner = 0
	excute_group = y['Group-Excute3'].value
	if excute_group:
		ExcuteGroup = 1
	else:
		ExcuteGroup = 0
	excute_other = y['Other-Excute3'].value
	if excute_other:
		ExcuteOther = 1
	else:
		ExcuteOther = 0
	
	# Total
	OwnerTotal = ReadOwner + WriteOwner + ExcuteOwner
	GroupTotal = ReadGroup + WriteGroup + ExcuteGroup
	OtherTotal = ReadOther + WriteOther + ExcuteOther
	
	# Owner Total String
	if OwnerTotal == 7:
		Total_Owner_String = '-rwx'
	if OwnerTotal == 6:
		Total_Owner_String = '-rw-'
	if OwnerTotal == 5:
		Total_Owner_String = '-r-x'
	if OwnerTotal == 4:
		Total_Owner_String = '-r--'
	if OwnerTotal == 3:
		Total_Owner_String = '--wx'
	if OwnerTotal == 2:
		Total_Owner_String = '--w-'
	if OwnerTotal == 1:
		Total_Owner_String = '---x'
	if OwnerTotal == 0:
		Total_Owner_String = '----'
		
	# Group Total String
	if GroupTotal == 7:
		Total_Group_String = 'rwx'
	if GroupTotal == 6:
		Total_Group_String = 'rw-'
	if GroupTotal == 5:
		Total_Group_String = 'r-x'
	if GroupTotal == 4:
		Total_Group_String = 'r--'
	if GroupTotal == 3:
		Total_Group_String = '-wx'
	if GroupTotal == 2:
		Total_Group_String = '-w-'
	if GroupTotal == 1:
		Total_Group_String = '--x'
	if GroupTotal == 0:
		Total_Group_String = '---'
		
	# Other Total String
	if OtherTotal == 7:
		Total_Other_String = 'rwx'
	if OtherTotal == 6:
		Total_Other_String = 'rw-'
	if OtherTotal == 5:
		Total_Other_String = 'r-x'
	if OtherTotal == 4:
		Total_Other_String = 'r--'
	if OtherTotal == 3:
		Total_Other_String = '-wx'
	if OtherTotal == 2:
		Total_Other_String = '-w-'
	if OtherTotal == 1:
		Total_Other_String = '--x'
	if OtherTotal == 0:
		Total_Other_String = '---'
		
	TotalCalc = """{OT}{GT}{OTT}""".format(OT=OwnerTotal, GT=GroupTotal, OTT=OtherTotal)
	
	Total_String = """{SOT}{SGT}{SOTT}""".format(SOT=Total_Owner_String, SGT=Total_Group_String, SOTT=Total_Other_String)
	
	TotalS = sender.superview['TopView']
	TotalS.text = TotalCalc
	TotalStringS = sender.superview['TopView2']
	TotalStringS.text = Total_String

v = ui.load_view()
v.present('sheet')
