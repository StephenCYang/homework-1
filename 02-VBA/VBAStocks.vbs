'VBAStocks

Sub Moderate()

' VARIABLE DECLARATION
Dim total_stock_vol As Double
Dim i As Long
Dim change As Single
Dim j As Integer
Dim start As Long
Dim row_count As Long
Dim percent_change As Single

' SET NEW HEADERS FOR OUTPUT
    Range("I1").Value = "Ticker Symbol"
    Range("J1").Value = "Yearly Change"
    Range("K1").Value = "OpenClose Percent Change"
    Range("L1").Value = "Stotal Stock Volume"

' SET STARTING VALUES
j = 0
total_stock_vol = 0
change = 0
start = 2 'THIS IS SET TO '2' BECAUSE THE DATA STARTS AT THE SECOND ROW

' GET THE LAST ROW IN THE DATA AND STORE IT INTO "row_count"
row_count = Cells(Rows.Count, "A").End(xlUp).Row


For i = 2 To row_count
    'TRACK CHANGES ONCE THE STOCK TICKER CHANGES
    If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
        total_stock_vol = total_stock_vol + Cells(i, 7).Value
    
    ' MANAGE VALUES THAT = TO ZERO
        If total_stock_vol = 0 Then
            Range("I" & 2 + j).Value = Cells(i, 1).Value
            Range("J" & 2 + j).Value = 0
            Range("K" & 2 + j).Value = "%" & 0
            Range("L" & 2 + j).Value = 0
        Else
            'LOOK FOR THE ZERO
            If Cells(start, 3) = 0 Then
                For find_value = start To i
                    If Cells(find_value, 3).Value <> 0 Then
                        start = find_value
                        Exit For
                    End If
                Next find_value
            End If

            'CALCULATE THE PERCENT CHANGE
            change = (Cells(i, 6) - Cells(start, 3))
            percent_change = Round((change / Cells(start, 3) * 100), 2)

            'MOVE TO THE NEXT STOCK TICKER
            start = i + 1

            'PRINT
            Range("I" & 2 + j).Value = Cells(i, 1).Value
            Range("J" & 2 + j).Value = Round(change, 2)
            Range("K" & 2 + j).Value = "%" & percent_change
            Range("L" & 2 + j).Value = total_stock_vol

            'FORMAT THE RESULTS TO LOOK NICE
            Select Case change
                Case Is > 0
                    Range("J" & 2 + j).Interior.ColorIndex = 4
                Case Is < 0
                    Range("J" & 2 + j).Interior.ColorIndex = 3
                Case Else
                    Range("J" & 2 + j).Interior.ColorIndex = 0
            End Select
        End If

        'RESET COUNTERS TO ZERO FOR THE NEXT ROUND OF ITERATIONS THROUGH THE STOCK TICKERS
        Total = 0
        change = 0
        j = j + 1

    Else
        total_stock_vol = total_stock_vol + Cells(i, 7).Value
    End If

Next i

End Sub

