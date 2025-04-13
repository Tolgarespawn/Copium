#!/usr/bin/tclsh

package require Tk

set theme [lindex $::argv 0]

# Eğer tema dosyası varsa, kaynak dosyayı yükle
if { [file exists "$theme.tcl"] } {
  source "$theme.tcl"
}

# Temayı uygula
ttk::style theme use $theme

# TFrame stilinin arka plan rengini al
set tbg [ttk::style lookup TFrame -background]
lassign [winfo rgb . $tbg] bg_r bg_g bg_b

# RGB değerlerini hex formatına çevir
set tbg [format {#%02x%02x%02x} \
  [expr {$bg_r / 256}] \
  [expr {$bg_g / 256}] \
  [expr {$bg_b / 256}]]

# Ana pencerenin arka plan rengini ayarla
. configure -background $tbg

# Değişkenleri başlat
set val 55
set valb $theme
set off 0
set on 1

# Notebook widget'ını oluştur ve bazı frame'ler ekle
ttk::notebook .nb
pack .nb -side left -fill both -expand true

# Tema adıyla bir labelframe oluştur
ttk::labelframe .lf -text " $theme "
.nb add .lf -text $theme

# Tema adını tersten yazıp başka bir frame'de göster
ttk::frame .junk
.nb add .junk -text [join [lreverse [split $theme {}]] {}]

# Tema adıyla bir label ve buton ekle
ttk::frame .bf
ttk::label .lb -text $theme
ttk::button .b -text $theme
pack .lb .b -in .bf -side left -padx 3p

# Önceden tanımlı değerlerle bir combobox oluştur
ttk::combobox .combo -values [list aaa bbb ccc] -textvariable valb -width 15

# "On" ve "Off" seçenekleriyle checkbutton ekle
ttk::frame .cbf
ttk::checkbutton .cboff -text off -variable off
ttk::checkbutton .cbon -text on -variable on
pack .cboff .cbon -in .cbf -side left -padx 3p

# Bir separator ekle
ttk::separator .sep

# Radio button'lar ekle
ttk::frame .rbf
ttk::radiobutton .rboff -text off -variable on -value 0
ttk::radiobutton .rbon -text on -variable on -value 1
pack .rboff .rbon -in .rbf -side left -padx 3p

# Scale, progress bar, entry, spinbox ve scrollbar ekle
ttk::scale .sc -from 0 -to 100 -variable val
ttk::progressbar .pb -mode determinate -length 100 -variable val
ttk::entry .ent -textvariable valb -width 15
ttk::spinbox .sbox -textvariable val -width 5
ttk::scrollbar .sb

# Sağ alt köşeye bir size grip ekle
ttk::sizegrip .sg

# Widget'ları pencereye yerleştir
pack .sb -side right -fill y -expand true
pack .bf .combo .cbf .sep .rbf .sc .pb .ent .sbox \
    -in .lf -side top -anchor w -padx 3p -pady 3p
pack configure .sep -fill x -expand true
pack .sg -in .lf -side right -anchor s
