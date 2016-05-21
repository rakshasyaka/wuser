$dir_path = "D:\PROJECTS\PYTHON\WUSER\"
#ls D:\PROJECTS\PYTHON\WUSER

$all_updates = Import-Clixml "D:\PROJECTS\PYTHON\WUSER\all_updates.xml"

$rules_list = Get-Content "$dir_path\auto_rules.txt"
foreach($rule in $rules_list){
    Write-Host $rule -ForegroundColor Yellow
    $ciid_upd_list = Get-Content $dir_path\$rule
    $hash_for_json = @{}
    foreach($ciid_upd in $ciid_upd_list){
        $upd = $all_updates | where {$_.ci_id -eq $ciid_upd}
        $art_id = $upd.ArticleID
        if(($art_id -eq $null) -or ($art_id -eq $false) -or ($art_id.length -lt 3)){continue}
        else{
            $date_last_modified = $upd.DateLastModified
            $cat_and_prod = $upd.LocalizedCategoryInstanceNames
            $hash_upd = @{"last_modif" = $date_last_modified; "category" = $cat_and_prod[0]; "product" = $cat_and_prod[1]}
            try{
                $hash_for_json.Add($art_id, $hash_upd) 
                }
            catch{
                $hash_for_json[$art_id]
                }
            }
    }
   ConvertTo-Json $hash_for_json | Out-File $dir_path\$rule".json"
}


# working example
#$try_json = (New-Object PSObject |
#   Add-Member -PassThru NoteProperty Name 'John Doe' |
#   Add-Member -PassThru NoteProperty Age 10          |
#   Add-Member -PassThru NoteProperty Amount 10.1     |
#   Add-Member -PassThru NoteProperty MixedItems (1,2,3,"a") |
#   Add-Member -PassThru NoteProperty NumericItems (1,2,3) |
#   Add-Member -PassThru NoteProperty StringItems ("a","b","c")
#) | ConvertTo-JSON
#$test_dict = @{"updates" = @{"kb111" = @{"last_modif" = [datetime]"7/22/15"; "category" = "Critical"; "produc" = "windows 7"}; "kb222" = @{"last_modif" = [datetime]"8/15/14"; "category" = "security"; "produc" = "office 10"};}}
#$try_jason2 = ConvertTo-Json $test_dict
